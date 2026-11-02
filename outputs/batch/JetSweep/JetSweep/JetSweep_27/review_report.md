# Play-Annotation-Generator Annotation Review — JetSweep_27

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_27`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 26
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 4
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE-Y | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE-F | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `1` | `0` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_LeadBlock` | LB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `1` | `0` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `21` | `20` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `16` | `15` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `17` | `16` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `21` | `20` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `8` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LB | `10` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE-Y | `18` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE-F | `19` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `3` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 69 |
| ✅ EXACT | `Action_JetMotion` | WR | `1` | `0` | 17 | START | 17 | 99 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 62 | START | 62 | 75 |
| ✅ EXACT | `Action_LeadBlock` | LB | `10` | `9` | 70 | START | 70 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `16` | `15` | 70 | START | 70 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `16` | 70 | START | 76 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `20` | 70 | START | 70 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `8` | `7` | 70 | START | 70 | 76 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 75 | END | 62 | 75 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 88 | START | 88 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `1` | `0` | 100 | START | 100 | 222 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `21` | `20` | 100 | START | 100 | 137 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `16` | `15` | 137 | BOUNDARY | 81 | 137 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `17` | `16` | 137 | BOUNDARY | 81 | 137 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `21` | `20` | 137 | BOUNDARY | 100 | 137 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `8` | `7` | 137 | BOUNDARY | 78 | 137 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_SnapReceive` | 62 | 75 | 14 | inferred_complete_timeline |
| `Action_None` | 76 | 87 | 12 | inferred_complete_timeline |
| `Action_Toss` | 88 | 99 | 12 | inferred_complete_timeline |
| `Action_None` | 100 | 198 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_JetMotion` | 17 | 99 | 83 | inferred_complete_timeline |
| `Action_BallCarry` | 100 | 222 | 123 | inferred_complete_timeline |
| `Action_BallCarry` | 224 | 266 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 299 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>TE-F — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 230 | 169 | inferred_complete_timeline |
| `Action_None` | 232 | 245 | 14 | inferred_complete_timeline |
| `Action_None` | 248 | 251 | 4 | inferred_complete_timeline |
| `Action_None` | 254 | 256 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE-Y — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 73 | 12 | inferred_complete_timeline |
| `Action_None` | 75 | 142 | 68 | inferred_complete_timeline |
| `Action_None` | 146 | 156 | 11 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 76 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 137 | 60 | inferred_complete_timeline |
| `Action_None` | 138 | 264 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 79 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 137 | 57 | inferred_complete_timeline |
| `Action_None` | 138 | 240 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_BallSnap` | 62 | 75 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 137 | 57 | inferred_complete_timeline |
| `Action_None` | 138 | 253 | 116 | inferred_complete_timeline |
| `Action_None` | 257 | 299 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–281
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 73 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 99 | 13 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 100 | 137 | 38 | inferred_complete_timeline |
| `Action_None` | 138 | 281 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–262
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_LeadBlock` | 70 | 137 | 68 | inferred_complete_timeline |
| `Action_None` | 138 | 236 | 99 | inferred_complete_timeline |
| `Action_None` | 240 | 262 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 299 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 68 | 7 | inferred_complete_timeline |
| `Action_None` | 70 | 73 | 4 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_None` | 78 | 206 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 73 | 12 | inferred_complete_timeline |
| `Action_None` | 75 | 90 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 94 | 33 | inferred_complete_timeline |
| `Action_None` | 99 | 283 | 185 | inferred_complete_timeline |
| `Action_None` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_None` | 289 | 299 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 183 | 122 | inferred_complete_timeline |
| `Action_None` | 185 | 190 | 6 | inferred_complete_timeline |
| `Action_None` | 214 | 253 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 149 | 88 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_None` | 157 | 299 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 66 | 5 | inferred_complete_timeline |
| `Action_None` | 69 | 299 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>FS — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 285 | 224 | inferred_complete_timeline |
| `Action_None` | 287 | 294 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 154 | 93 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 299 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 142 | 81 | inferred_complete_timeline |
| `Action_None` | 169 | 226 | 58 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_None` | 232 | 267 | 36 | inferred_complete_timeline |
| `Action_None` | 270 | 272 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–299 | 300 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 91–257 | 163 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 93–99 | 7 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 118–119 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 177–299 | 119 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 180–228 | 49 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 205–247 | 43 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 275–286 | 12 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 277–299 | 20 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 291–299 | 4 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 294–299 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `LB` position mapped to `offense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 56: Duplicate assignment for track ID '22' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [62–75], lower_priority='Action_ZoneBlock' annotated_start=70, effective_Action_ZoneBlock_start=76.
- ⚠️ Action 'Action_BallCarry' range [100-222] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [224-266] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-73] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-90] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-285] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-294] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-94] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-283] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-76] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-264] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-68] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-73] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-206] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-236] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-262] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-198] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-154] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-183] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-190] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-253] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-142] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-226] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-267] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-79] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-240] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [62-75] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '16' starts at frame 76, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [76-76] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-253] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-73] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-142] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-156] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-230] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-245] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-73] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-80] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-85] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-281] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-66] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-299] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-257] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-99] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-289] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-228] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-247] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-286] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-294] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '30' has 1 frames without a visible bounding box.
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

</details>