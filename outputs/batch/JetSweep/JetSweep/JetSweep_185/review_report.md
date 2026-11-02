# Play-Annotation-Generator Annotation Review — JetSweep_185

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_185`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `3` | `2` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `2` | `1` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Toss` | QB | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 76 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `3` | `2` | 41 | START | 41 | 105 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 74 | START | 74 | 92 |
| ✅ EXACT | `Action_LeadBlock` | TE | `2` | `1` | 77 | START | 77 | 203 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `11` | `10` | 77 | START | 93 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `14` | `13` | 77 | START | 77 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `18` | 77 | START | 77 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `19` | 77 | START | 77 | 85 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `4` | 77 | START | 77 | 204 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 92 | END | 74 | 92 |
| ✅ EXACT | `Action_Toss` | QB | `18` | `17` | 97 | START | 97 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `3` | `2` | 106 | START | 106 | 186 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 204 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–217
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_SnapReceive` | 74 | 92 | 19 | inferred_complete_timeline |
| `Action_None` | 93 | 96 | 4 | inferred_complete_timeline |
| `Action_Toss` | 97 | 105 | 9 | inferred_complete_timeline |
| `Action_None` | 106 | 217 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 176 | 103 | inferred_complete_timeline |
| `Action_None` | 178 | 238 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 329 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_JetMotion` | 41 | 105 | 65 | inferred_complete_timeline |
| `Action_BallCarry` | 106 | 186 | 81 | inferred_complete_timeline |
| `Action_BallCarry` | 203 | 293 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_LeadBlock` | 77 | 203 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 173 | 97 | inferred_complete_timeline |
| `Action_ZoneBlock` | 177 | 204 | 28 | inferred_complete_timeline |
| `Action_None` | 205 | 251 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 85 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 100 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 152 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_BallSnap` | 74 | 92 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 96 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 149 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 152 | 204 | 53 | inferred_complete_timeline |
| `Action_None` | 205 | 229 | 25 | inferred_complete_timeline |
| `Action_None` | 231 | 243 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–276
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 204 | 128 | inferred_complete_timeline |
| `Action_None` | 205 | 207 | 3 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 225 | 13 | inferred_complete_timeline |
| `Action_None` | 229 | 242 | 14 | inferred_complete_timeline |
| `Action_None` | 247 | 276 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 93 | 20 | inferred_complete_timeline |
| `Action_None` | 100 | 102 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–273
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 273 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 254 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 153 | 80 | inferred_complete_timeline |
| `Action_None` | 188 | 205 | 18 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 152 | 79 | inferred_complete_timeline |
| `Action_None` | 154 | 329 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 73 | 35 | inferred_complete_timeline |
| `Action_None` | 74 | 284 | 211 | inferred_complete_timeline |
| `Action_None` | 293 | 295 | 3 | inferred_complete_timeline |
| `Action_None` | 301 | 304 | 4 | inferred_complete_timeline |
| `Action_None` | 310 | 315 | 6 | inferred_complete_timeline |
| `Action_None` | 318 | 329 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 204 | 131 | inferred_complete_timeline |
| `Action_None` | 206 | 329 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 203 | 130 | inferred_complete_timeline |
| `Action_None` | 207 | 213 | 7 | inferred_complete_timeline |
| `Action_None` | 232 | 237 | 6 | inferred_complete_timeline |
| `Action_None` | 245 | 263 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 288 | 215 | inferred_complete_timeline |
| `Action_None` | 297 | 302 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 127 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 220 | 147 | inferred_complete_timeline |
| `Action_None` | 222 | 241 | 20 | inferred_complete_timeline |
| `Action_None` | 243 | 329 | 87 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 62–239 | 92 | 6 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 134–291 | 158 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 148–152 | 5 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 158–257 | 90 | 4 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 169–204 | 34 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 183–243 | 61 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 190–295 | 106 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 251–324 | 72 | 3 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 321–329 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `11` (C): Annotated start 77 != Inferred start 93
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '1' (TE) duration 127 frames exceeds threshold 90 frames [start=77, end=203].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (RT) duration 128 frames exceeds threshold 90 frames [start=77, end=204].
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [74–92], lower_priority='Action_ZoneBlock' annotated_start=77, effective_Action_ZoneBlock_start=93.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (LT) duration 128 frames exceeds threshold 90 frames [start=77, end=204].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (RG) duration 128 frames exceeds threshold 90 frames [start=77, end=204].
- ⚠️ Action 'Action_None' range [74-288] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-302] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [77-203] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [106-186] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [203-293] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-176] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-238] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-225] for track '4' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-242] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-276] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-273] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-153] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-205] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-284] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-304] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-315] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-254] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-96] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-203] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-213] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-237] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-263] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-93] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-173] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-251] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-220] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-241] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-127] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-217] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-149] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-229] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-243] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-85] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-100] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-152] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-204] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-66] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-90] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-139] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-159] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-209] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-291] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-204] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-237] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-257] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-204] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-243] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-295] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-260] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-324] for track '29' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.

</details>