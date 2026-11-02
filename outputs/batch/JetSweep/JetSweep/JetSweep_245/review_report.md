# Play-Annotation-Generator Annotation Review — JetSweep_245

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_245`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 9
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `9` | `8` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Toss` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `17` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `9` | `8` | 1 | START | 1 | 44 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 23 | START | 23 | 35 |
| ✅ EXACT | `Action_LeadBlock` | TE | `18` | `17` | 25 | START | 25 | 99 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `16` | `15` | 25 | START | 25 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `18` | 25 | START | 36 | 118 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `20` | `19` | 25 | START | 25 | 50 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `22` | `21` | 25 | START | 25 | 118 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `3` | 25 | START | 25 | 118 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 35 | END | 23 | 35 |
| ✅ EXACT | `Action_Toss` | QB | `15` | `14` | 40 | START | 40 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `9` | `8` | 45 | START | 45 | 205 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 118 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_SnapReceive` | 23 | 35 | 13 | inferred_complete_timeline |
| `Action_None` | 36 | 39 | 4 | inferred_complete_timeline |
| `Action_Toss` | 40 | 44 | 5 | inferred_complete_timeline |
| `Action_None` | 45 | 75 | 31 | inferred_complete_timeline |
| `Action_None` | 78 | 81 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 72 | 50 | inferred_complete_timeline |
| `Action_None` | 74 | 166 | 93 | inferred_complete_timeline |
| `Action_None` | 170 | 239 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 239 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_JetMotion` | 1 | 44 | 44 | inferred_complete_timeline |
| `Action_BallCarry` | 45 | 205 | 161 | inferred_complete_timeline |
| `Action_BallCarry` | 207 | 209 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 138 | 116 | inferred_complete_timeline |
| `Action_None` | 143 | 156 | 14 | inferred_complete_timeline |
| `Action_None` | 164 | 194 | 31 | inferred_complete_timeline |
| `Action_None` | 205 | 214 | 10 | inferred_complete_timeline |
| `Action_None` | 222 | 239 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_LeadBlock` | 25 | 99 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 118 | 94 | inferred_complete_timeline |
| `Action_None` | 119 | 239 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 118 | 94 | inferred_complete_timeline |
| `Action_None` | 119 | 239 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_BallSnap` | 23 | 35 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 118 | 83 | inferred_complete_timeline |
| `Action_None` | 119 | 177 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 50 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 118 | 94 | inferred_complete_timeline |
| `Action_None` | 119 | 239 | 121 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 239 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 239 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 82 | 60 | inferred_complete_timeline |
| `Action_None` | 105 | 129 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 239 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 239 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 77 | 55 | inferred_complete_timeline |
| `Action_None` | 79 | 239 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 180 | 158 | inferred_complete_timeline |
| `Action_None` | 187 | 200 | 14 | inferred_complete_timeline |
| `Action_None` | 213 | 239 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 218 | 196 | inferred_complete_timeline |
| `Action_None` | 220 | 226 | 7 | inferred_complete_timeline |
| `Action_None` | 230 | 239 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 40 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 226 | 204 | inferred_complete_timeline |
| `Action_None` | 228 | 238 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 96 | 74 | inferred_complete_timeline |
| `Action_None` | 99 | 108 | 10 | inferred_complete_timeline |
| `Action_None` | 112 | 226 | 115 | inferred_complete_timeline |
| `Action_None` | 228 | 235 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 39–153 | 113 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 76–86 | 10 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 107–239 | 133 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 113–239 | 126 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 115–139 | 9 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 143–144 | 2 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 148–239 | 92 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 159–179 | 6 | 3 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 160–163 | 4 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 168–171 | 4 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 169–172 | 4 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 173–176 | 4 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 175–183 | 9 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 185–239 | 55 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 186–239 | 54 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 191–239 | 49 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 197–198 | 2 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 208–209 | 2 | 1 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 235–239 | 5 | 1 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 236–238 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (LT) duration 94 frames exceeds threshold 90 frames [start=25, end=118].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (LG) duration 94 frames exceeds threshold 90 frames [start=25, end=118].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (C) duration 94 frames exceeds threshold 90 frames [start=25, end=118].
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [23–35], lower_priority='Action_ZoneBlock' annotated_start=25, effective_Action_ZoneBlock_start=36.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 94 frames exceeds threshold 90 frames [start=25, end=118].
- ⚠️ Action 'Action_None' range [23-218] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-226] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-72] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-166] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-77] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-226] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-238] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-200] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [45-205] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [207-209] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-82] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-129] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-96] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-108] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-226] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-235] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-75] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-81] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-156] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-194] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-214] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [25-99] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-177] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-50] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-40] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-147] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-79] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-86] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-239] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-163] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-183] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '42' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.

</details>