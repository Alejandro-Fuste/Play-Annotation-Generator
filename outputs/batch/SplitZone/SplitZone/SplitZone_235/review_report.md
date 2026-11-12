# Play-Annotation-Generator Annotation Review — SplitZone_235

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_235`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 0 | START | 0 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 140 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 141 | START | 141 | 157 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `10` | 144 | START | 144 | 243 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `13` | `13` | 144 | START | 144 | 243 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 144 | START | 158 | 161 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `16` | `16` | 144 | START | 144 | 234 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 144 | START | 144 | 157 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 157 | END | 141 | 157 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `12` | 159 | START | 159 | 170 |
| ✅ EXACT | `Action_SplitBlock` | TE | `0` | `0` | 160 | START | 160 | 183 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `5` | 171 | START | 171 | 282 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 243 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_SnapReceive` | 141 | 157 | 17 | inferred_complete_timeline |
| `Action_None` | 158 | 158 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 159 | 170 | 12 | inferred_complete_timeline |
| `Action_None` | 171 | 297 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_BallCarry` | 171 | 282 | 112 | inferred_complete_timeline |
| `Action_BallCarry` | 284 | 329 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 329 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 329 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 329 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_SplitBlock` | 160 | 183 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 243 | 100 | inferred_complete_timeline |
| `Action_None` | 244 | 325 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 234 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_BallSnap` | 141 | 157 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 165 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 17 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 21 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 50 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 123 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 157 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 182 | 184 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 201 | 205 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 218 | 243 | 26 | inferred_complete_timeline |
| `Action_None` | 244 | 329 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 243 | 100 | inferred_complete_timeline |
| `Action_None` | 244 | 291 | 48 | inferred_complete_timeline |
| `Action_None` | 294 | 299 | 6 | inferred_complete_timeline |
| `Action_None` | 301 | 329 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 161 | 21 | inferred_complete_timeline |
| `Action_None` | 175 | 328 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 140 | 92 | inferred_complete_timeline |
| `Action_None` | 141 | 207 | 67 | inferred_complete_timeline |
| `Action_None` | 220 | 277 | 58 | inferred_complete_timeline |
| `Action_None` | 293 | 294 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 223 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 195 | 55 | inferred_complete_timeline |
| `Action_None` | 197 | 329 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 175 | 35 | inferred_complete_timeline |
| `Action_None` | 178 | 183 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 329 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 329 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 298 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 284 | 144 | inferred_complete_timeline |
| `Action_None` | 286 | 288 | 3 | inferred_complete_timeline |
| `Action_None` | 290 | 329 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 329 | 189 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–290 | 260 | 5 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–28 | 18 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 23–31 | 7 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 64–186 | 9 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 199–201 | 3 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 200–329 | 113 | 7 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 200–329 | 105 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 202–327 | 36 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 209–329 | 121 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 228–311 | 80 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 255–256 | 2 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 257–299 | 40 | 2 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 303–312 | 10 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 304–326 | 23 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 311–326 | 16 | 1 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 319–324 | 6 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 324–329 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 72 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RT) duration 100 frames exceeds threshold 90 frames [start=144, end=243].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (LT) duration 100 frames exceeds threshold 90 frames [start=144, end=243].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [141–157], lower_priority='Action_ZoneBlock' annotated_start=144, effective_Action_ZoneBlock_start=158.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (LG) duration 91 frames exceeds threshold 90 frames [start=144, end=234].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 100 frames exceeds threshold 90 frames [start=144, end=243].
- ⚠️ Action 'Action_SplitBlock' range [160-183] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-298] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-284] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [171-282] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [284-329] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-195] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-223] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-243] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-291] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-297] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 244, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [244-325] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [158-161] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [164-165] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-234] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-329] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-161] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-328] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-277] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-140] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-207] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-277] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-17] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-21] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-50] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-143] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-157] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [182-184] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [201-205] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-329] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-24] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-28] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-27] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-234] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-262] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-284] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-329] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-207] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-327] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-305] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-261] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-299] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-312] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-326] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-326] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-324] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>