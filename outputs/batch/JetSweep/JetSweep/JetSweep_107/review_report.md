# Play-Annotation-Generator Annotation Review — JetSweep_107

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_107`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_LeadBlock` | TE1 | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `21` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `1` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `10` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 131 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 132 | START | 132 | 154 |
| ✅ EXACT | `Action_LeadBlock` | TE1 | `10` | `9` | 135 | START | 135 | 219 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `10` | 135 | START | 135 | 208 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `12` | `11` | 135 | START | 135 | 219 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `13` | `12` | 135 | START | 155 | 212 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `3` | `2` | 135 | START | 135 | 169 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `4` | 135 | START | 135 | 219 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `21` | `19` | 154 | START | 154 | 177 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 154 | END | 132 | 154 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 160 | START | 160 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `21` | `19` | 178 | START | 178 | 179 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 219 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_SnapReceive` | 132 | 154 | 23 | inferred_complete_timeline |
| `Action_None` | 155 | 159 | 5 | inferred_complete_timeline |
| `Action_Toss` | 160 | 177 | 18 | inferred_complete_timeline |
| `Action_None` | 178 | 204 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_LeadBlock` | 135 | 219 | 85 | inferred_complete_timeline |
| `Action_None` | 220 | 336 | 117 | inferred_complete_timeline |
| `Action_None` | 338 | 359 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_None` | 132 | 171 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_None` | 132 | 195 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 219 | 85 | inferred_complete_timeline |
| `Action_None` | 220 | 238 | 19 | inferred_complete_timeline |
| `Action_None` | 329 | 359 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 219 | 85 | inferred_complete_timeline |
| `Action_None` | 220 | 220 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_BallSnap` | 132 | 154 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 212 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 208 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 169 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 192 | 204 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_None` | 132 | 155 | 24 | inferred_complete_timeline |
| `Action_None` | 178 | 195 | 18 | inferred_complete_timeline |
| `Action_None` | 202 | 221 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–8
- **Visible Samples:** 9

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_None` | 132 | 153 | 22 | inferred_complete_timeline |
| `Action_None` | 159 | 359 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_None` | 132 | 147 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_None` | 132 | 166 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_None` | 132 | 172 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_None` | 132 | 181 | 50 | inferred_complete_timeline |
| `Action_None` | 206 | 216 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_None` | 132 | 280 | 149 | inferred_complete_timeline |
| `Action_None` | 286 | 356 | 71 | inferred_complete_timeline |
| `Action_None` | 358 | 359 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 131 | 12 | inferred_complete_timeline |
| `Action_None` | 132 | 186 | 55 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 6–200 | 185 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 154–313 | 156 | 5 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 173–206 | 34 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 178–195 | 18 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 182–256 | 74 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 203–359 | 157 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 207–359 | 137 | 7 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 209–263 | 55 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 214–218 | 5 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 247–359 | 113 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 260–273 | 14 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 276–359 | 84 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 281–359 | 76 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 287–359 | 67 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 298–336 | 25 | 3 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 299–314 | 13 | 2 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 309–312 | 4 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 310–359 | 50 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 310–359 | 50 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 315–359 | 45 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 317–359 | 43 | 1 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 326–342 | 11 | 2 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 334–336 | 3 | 1 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 340–359 | 20 | 1 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 351–359 | 9 | 1 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 351–359 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `13` (C): Annotated start 135 != Inferred start 155
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [132–154], lower_priority='Action_ZoneBlock' annotated_start=135, effective_Action_ZoneBlock_start=155.
- ⚠️ Action 'Action_None' range [132-195] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-280] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-356] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [135-169] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [192-204] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-181] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-216] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-238] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-172] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-171] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-204] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-166] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [135-219] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-336] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [135-208] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 220, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [220-220] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [155-212] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-118] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-195] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-221] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-153] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-359] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-154] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-200] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [178-179] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [181-248] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [251-309] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [311-313] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-206] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-195] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-237] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-256] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-359] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-243] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-257] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-293] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-318] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-327] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-263] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-273] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-289] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-339] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-313] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-336] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-309] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-312] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-334] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-336] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-359] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.

</details>