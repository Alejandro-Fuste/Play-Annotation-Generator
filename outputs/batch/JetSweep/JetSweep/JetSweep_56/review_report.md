# Play-Annotation-Generator Annotation Review — JetSweep_56

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_56`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 96
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `5` | `4` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_LeadBlock` | WR2 | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Toss` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `21` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 122 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `5` | `4` | 91 | START | 91 | 147 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 123 | START | 123 | 138 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `9` | 130 | START | 130 | 153 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `12` | `11` | 130 | START | 130 | 153 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `18` | `17` | 130 | START | 130 | 153 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 130 | START | 130 | 158 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `22` | `21` | 130 | START | 139 | 152 |
| ✅ EXACT | `Action_LeadBlock` | WR2 | `3` | `2` | 132 | START | 132 | 153 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 138 | END | 123 | 138 |
| ✅ EXACT | `Action_Toss` | QB | `14` | `13` | 140 | START | 140 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `5` | `4` | 148 | START | 148 | 262 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 153 | BOUNDARY | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `21` | `20` | 159 | START | 159 | 258 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_SnapReceive` | 123 | 138 | 16 | inferred_complete_timeline |
| `Action_None` | 139 | 139 | 1 | inferred_complete_timeline |
| `Action_Toss` | 140 | 147 | 8 | inferred_complete_timeline |
| `Action_None` | 148 | 248 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 239 | 117 | inferred_complete_timeline |
| `Action_None` | 241 | 287 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–292
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_JetMotion` | 91 | 147 | 57 | inferred_complete_timeline |
| `Action_BallCarry` | 148 | 262 | 115 | inferred_complete_timeline |
| `Action_BallCarry` | 264 | 284 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 286 | 292 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_LeadBlock` | 132 | 153 | 22 | inferred_complete_timeline |
| `Action_None` | 154 | 294 | 141 | inferred_complete_timeline |
| `Action_None` | 298 | 304 | 7 | inferred_complete_timeline |
| `Action_None` | 308 | 329 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 261 | 139 | inferred_complete_timeline |
| `Action_None` | 267 | 289 | 23 | inferred_complete_timeline |
| `Action_None` | 301 | 308 | 8 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_None` | 318 | 329 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 270 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 153 | 24 | inferred_complete_timeline |
| `Action_None` | 154 | 157 | 4 | inferred_complete_timeline |
| `Action_None` | 159 | 275 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–283
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 153 | 24 | inferred_complete_timeline |
| `Action_None` | 154 | 167 | 14 | inferred_complete_timeline |
| `Action_None` | 169 | 283 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–319
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 122 | 38 | inferred_complete_timeline |
| `Action_BallSnap` | 123 | 138 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 152 | 14 | inferred_complete_timeline |
| `Action_None` | 156 | 319 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–306
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 158 | 29 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 159 | 258 | 100 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 260 | 306 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 153 | 24 | inferred_complete_timeline |
| `Action_None` | 154 | 171 | 18 | inferred_complete_timeline |
| `Action_None` | 173 | 329 | 157 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 169 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 240 | 118 | inferred_complete_timeline |
| `Action_None` | 242 | 329 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–313
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 266 | 144 | inferred_complete_timeline |
| `Action_None` | 268 | 313 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–300
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 300 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–306
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 301 | 179 | inferred_complete_timeline |
| `Action_None` | 304 | 306 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 202 | 80 | inferred_complete_timeline |
| `Action_None` | 207 | 233 | 27 | inferred_complete_timeline |
| `Action_None` | 235 | 239 | 5 | inferred_complete_timeline |
| `Action_None` | 244 | 329 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 302 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 329 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 298 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–285
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 285 | 163 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–304 | 297 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 141–154 | 14 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 151–152 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 156–197 | 6 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 167–176 | 8 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 183–279 | 97 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 192–200 | 6 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 203–204 | 2 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 209–212 | 4 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 214–215 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 219–220 | 2 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 246–278 | 11 | 3 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 270–271 | 2 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 302–329 | 28 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 323–329 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `22` (C): Annotated start 130 != Inferred start 139
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 114: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '20' (RG) duration 148 frames exceeds threshold 90 frames [start=159, end=306].
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [123–138], lower_priority='Action_ZoneBlock' annotated_start=130, effective_Action_ZoneBlock_start=139.
- ⚠️ Action 'Action_None' range [123-265] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-286] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-296] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-304] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-270] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-294] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-304] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [148-262] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [264-284] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [286-292] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-202] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-233] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-261] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-289] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-308] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-329] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-302] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-301] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-306] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-171] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-298] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-167] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-283] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-287] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-248] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-240] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-169] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-285] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-275] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-300] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-266] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-313] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [159-258] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [260-306] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-122] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [139-152] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-319] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-154] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-279] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-256] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-329] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>