# Play-Annotation-Generator Annotation Review — JetSweep_195

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_195`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 96
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
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `4` | `3` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ✅ EXACT | `Action_LeadBlock` | WR1 | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 81 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `4` | `3` | 43 | START | 43 | 106 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 82 | START | 82 | 96 |
| ✅ EXACT | `Action_LeadBlock` | WR1 | `1` | `0` | 83 | START | 83 | 230 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `16` | `15` | 83 | START | 83 | 230 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 83 | START | 83 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `19` | 83 | START | 97 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `20` | 83 | START | 83 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 83 | START | 83 | 100 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 96 | END | 82 | 96 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 99 | START | 99 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `4` | `3` | 107 | START | 107 | 224 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 230 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–256
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_SnapReceive` | 82 | 96 | 15 | inferred_complete_timeline |
| `Action_None` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_Toss` | 99 | 106 | 8 | inferred_complete_timeline |
| `Action_None` | 107 | 198 | 92 | inferred_complete_timeline |
| `Action_None` | 204 | 256 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 238 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_LeadBlock` | 83 | 230 | 148 | inferred_complete_timeline |
| `Action_None` | 235 | 269 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_JetMotion` | 43 | 106 | 64 | inferred_complete_timeline |
| `Action_BallCarry` | 107 | 224 | 118 | inferred_complete_timeline |
| `Action_BallCarry` | 228 | 229 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 152 | 71 | inferred_complete_timeline |
| `Action_None` | 154 | 157 | 4 | inferred_complete_timeline |
| `Action_None` | 163 | 165 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 269 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 230 | 148 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_None` | 235 | 246 | 12 | inferred_complete_timeline |
| `Action_None` | 248 | 250 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 119 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 152 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 215 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 220 | 230 | 11 | inferred_complete_timeline |
| `Action_None` | 231 | 254 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_BallSnap` | 82 | 96 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 104 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 100 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 160 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 177 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–261
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 108 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 116 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 230 | 113 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_None` | 235 | 261 | 27 | inferred_complete_timeline |

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
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 269 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 254 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 201 | 120 | inferred_complete_timeline |
| `Action_None` | 203 | 237 | 35 | inferred_complete_timeline |
| `Action_None` | 241 | 258 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 120 | 39 | inferred_complete_timeline |
| `Action_None` | 122 | 266 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 258 | 177 | inferred_complete_timeline |
| `Action_None` | 260 | 263 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 269 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 179 | 98 | inferred_complete_timeline |
| `Action_None` | 181 | 183 | 3 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 175 | 94 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 183 | 3 | inferred_complete_timeline |
| `Action_None` | 186 | 192 | 7 | inferred_complete_timeline |
| `Action_None` | 196 | 202 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–260
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 260 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 269 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–256
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 256 | 175 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 94–252 | 96 | 5 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 113–124 | 12 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 117–135 | 19 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 178–246 | 41 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 190–202 | 10 | 2 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 209–263 | 8 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 216–235 | 20 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 222–254 | 5 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 223–247 | 8 | 3 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 242–245 | 4 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 261–263 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '0' (WR1) duration 148 frames exceeds threshold 90 frames [start=83, end=230].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (LT) duration 148 frames exceeds threshold 90 frames [start=83, end=230].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (LG) duration 148 frames exceeds threshold 90 frames [start=83, end=230].
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [82–96], lower_priority='Action_ZoneBlock' annotated_start=83, effective_Action_ZoneBlock_start=97.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (RT) duration 148 frames exceeds threshold 90 frames [start=83, end=230].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 95 frames exceeds threshold 90 frames [start=83, end=177].
- ⚠️ Action 'Action_LeadBlock' range [83-230] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-238] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [107-224] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [228-229] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-201] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-237] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-258] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-152] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-120] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-266] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-198] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-256] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-254] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-258] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-263] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-179] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-175] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-192] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-246] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-260] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-256] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-119] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-152] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [158-215] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-254] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-104] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-108] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [111-116] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-230] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-261] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-100] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-160] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [162-177] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-110] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-207] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-252] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-124] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-135] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-201] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-220] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-263] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-235] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '32' has 1 frames without a visible bounding box.
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