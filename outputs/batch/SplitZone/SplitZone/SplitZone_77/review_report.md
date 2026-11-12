# Play-Annotation-Generator Annotation Review — SplitZone_77

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_77`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 58
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `8` | `8` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `11` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 20 | START | 21 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 20 | START | 21 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 20 | START | 21 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `15` | `Group` | 20 | START | 21 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 20 | START | 21 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `20` | `Group` | 20 | START | 21 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 20 | START | 21 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 20 | START | 21 | 194 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 20 | START | 21 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 20 | START | 21 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 20 | START | 21 | 186 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 187 | START | 187 | 204 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `12` | 190 | START | 205 | 259 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `13` | 190 | START | 190 | 210 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `18` | `18` | 190 | START | 190 | 302 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `5` | 190 | START | 190 | 302 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `8` | `8` | 190 | START | 190 | 211 |
| ✅ EXACT | `Action_SplitBlock` | TE | `4` | `4` | 195 | START | 195 | 302 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 204 | END | 187 | 204 |
| ✅ EXACT | `Action_BallCarry` | QB | `11` | `11` | 221 | START | 221 | 359 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 302 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 21–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 186 | 166 | inferred_complete_timeline |
| `Action_SnapReceive` | 187 | 204 | 18 | inferred_complete_timeline |
| `Action_None` | 205 | 220 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 221 | 359 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 21–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 186 | 166 | inferred_complete_timeline |
| `Action_None` | 187 | 359 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 21–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 186 | 166 | inferred_complete_timeline |
| `Action_None` | 187 | 359 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 21–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 186 | 166 | inferred_complete_timeline |
| `Action_None` | 187 | 359 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 21–359
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 186 | 166 | inferred_complete_timeline |
| `Action_None` | 187 | 315 | 129 | inferred_complete_timeline |
| `Action_None` | 318 | 319 | 2 | inferred_complete_timeline |
| `Action_None` | 321 | 322 | 2 | inferred_complete_timeline |
| `Action_None` | 324 | 359 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 21–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 194 | 174 | inferred_complete_timeline |
| `Action_SplitBlock` | 195 | 302 | 108 | inferred_complete_timeline |
| `Action_None` | 303 | 359 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 21–359
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 189 | 169 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 302 | 113 | inferred_complete_timeline |
| `Action_None` | 303 | 314 | 12 | inferred_complete_timeline |
| `Action_None` | 328 | 359 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 21–225
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 189 | 169 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 211 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 219 | 225 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 21–359
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 186 | 166 | inferred_complete_timeline |
| `Action_BallSnap` | 187 | 204 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 259 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 262 | 302 | 41 | inferred_complete_timeline |
| `Action_None` | 303 | 312 | 10 | inferred_complete_timeline |
| `Action_None` | 314 | 359 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 21–359
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 189 | 169 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 210 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 214 | 302 | 89 | inferred_complete_timeline |
| `Action_None` | 303 | 314 | 12 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |
| `Action_None` | 331 | 359 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 21–359
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 189 | 169 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 302 | 113 | inferred_complete_timeline |
| `Action_None` | 303 | 318 | 16 | inferred_complete_timeline |
| `Action_None` | 326 | 359 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 21–359
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 186 | 166 | inferred_complete_timeline |
| `Action_None` | 187 | 314 | 128 | inferred_complete_timeline |
| `Action_None` | 316 | 321 | 6 | inferred_complete_timeline |
| `Action_None` | 324 | 359 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 21–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 186 | 166 | inferred_complete_timeline |
| `Action_None` | 187 | 359 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 21–262
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 186 | 166 | inferred_complete_timeline |
| `Action_None` | 187 | 256 | 70 | inferred_complete_timeline |
| `Action_None` | 258 | 262 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 21–359
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 186 | 166 | inferred_complete_timeline |
| `Action_None` | 187 | 290 | 104 | inferred_complete_timeline |
| `Action_None` | 295 | 306 | 12 | inferred_complete_timeline |
| `Action_None` | 310 | 314 | 5 | inferred_complete_timeline |
| `Action_None` | 326 | 359 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 21–314
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 186 | 166 | inferred_complete_timeline |
| `Action_None` | 187 | 314 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 21–359
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 186 | 166 | inferred_complete_timeline |
| `Action_None` | 187 | 279 | 93 | inferred_complete_timeline |
| `Action_None` | 285 | 318 | 34 | inferred_complete_timeline |
| `Action_None` | 320 | 321 | 2 | inferred_complete_timeline |
| `Action_None` | 326 | 359 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 21–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 186 | 166 | inferred_complete_timeline |
| `Action_None` | 187 | 359 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 21–359
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 186 | 166 | inferred_complete_timeline |
| `Action_None` | 187 | 258 | 72 | inferred_complete_timeline |
| `Action_None` | 331 | 359 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 21–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 186 | 166 | inferred_complete_timeline |
| `Action_None` | 187 | 359 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 21–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 186 | 166 | inferred_complete_timeline |
| `Action_None` | 187 | 359 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 21–359
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 186 | 166 | inferred_complete_timeline |
| `Action_None` | 187 | 350 | 164 | inferred_complete_timeline |
| `Action_None` | 355 | 359 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 234–238 | 5 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 236–359 | 110 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 250–359 | 110 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 287–359 | 65 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 311–313 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `SAF1` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 42 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (RT) duration 113 frames exceeds threshold 90 frames [start=190, end=302].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (C) duration 113 frames exceeds threshold 90 frames [start=190, end=302].
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [187–204], lower_priority='Action_ZoneBlock' annotated_start=190, effective_Action_ZoneBlock_start=205.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (RG) duration 113 frames exceeds threshold 90 frames [start=190, end=302].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (LT) duration 113 frames exceeds threshold 90 frames [start=190, end=302].
- ⚠️ Action 'Action_None' range [187-256] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-314] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-321] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-359] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-315] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-302] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-318] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-290] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-306] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-314] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-350] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-211] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [219-225] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [205-259] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [262-302] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-312] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-210] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-314] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-258] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-359] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-314] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-302] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-314] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-279] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-318] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-359] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-314] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-359] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-314] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-313] for track '26' has 1 frames without a visible bounding box.
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

</details>