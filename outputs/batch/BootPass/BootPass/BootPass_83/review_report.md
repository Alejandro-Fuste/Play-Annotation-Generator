# Play-Annotation-Generator Annotation Review — BootPass_83

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_83`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 118
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `17` | `17` |
| ⚠️ START CHANGED | `Action_RunBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `23` | `22` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 37 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 28 | START | 28 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `17` | `17` | 38 | START | 38 | 48 |
| ⚠️ START CHANGED | `Action_RunBlock` | C | `18` | `18` | 38 | START | 45 | 47 |
| ✅ EXACT | `Action_RunBlock` | RG | `19` | `19` | 38 | START | 38 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `20` | `20` | 38 | START | 38 | 196 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `9` | `9` | 38 | START | 38 | 60 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 44 | END | 28 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | QB | `10` | `10` | 51 | START | 51 | 65 |
| ✅ EXACT | `Action_BootAway` | QB | `10` | `10` | 82 | START | 82 | 120 |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | `23` | `22` | 84 | START | 84 | 121 |
| ✅ EXACT | `Action_ThrowPass` | QB | `10` | `10` | 121 | START | 121 | 131 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `1` | `1` | 175 | START | 175 | 181 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_SnapReceive` | 28 | 44 | 17 | inferred_complete_timeline |
| `Action_None` | 45 | 50 | 6 | inferred_complete_timeline |
| `Action_FakeHandoff` | 51 | 65 | 15 | inferred_complete_timeline |
| `Action_FakeHandoff` | 70 | 81 | 12 | inferred_complete_timeline |
| `Action_BootAway` | 82 | 120 | 39 | inferred_complete_timeline |
| `Action_ThrowPass` | 121 | 131 | 11 | inferred_complete_timeline |
| `Action_None` | 132 | 254 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 299 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_SecureCatch` | 175 | 181 | 7 | inferred_complete_timeline |
| `Action_None` | 182 | 269 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 299 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_RunBlock` | 38 | 60 | 23 | inferred_complete_timeline |
| `Action_RunBlock` | 71 | 78 | 8 | inferred_complete_timeline |
| `Action_RunBlock` | 83 | 157 | 75 | inferred_complete_timeline |
| `Action_RunBlock` | 159 | 178 | 20 | inferred_complete_timeline |
| `Action_RunBlock` | 180 | 229 | 50 | inferred_complete_timeline |
| `Action_RunBlock` | 231 | 237 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 240 | 250 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_RunBlock` | 38 | 48 | 11 | inferred_complete_timeline |
| `Action_RunBlock` | 59 | 72 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_BallSnap` | 28 | 44 | 17 | inferred_complete_timeline |
| `Action_RunBlock` | 45 | 47 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_RunBlock` | 38 | 133 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_RunBlock` | 38 | 196 | 159 | inferred_complete_timeline |
| `Action_RunBlock` | 201 | 246 | 46 | inferred_complete_timeline |
| `Action_RunBlock` | 248 | 256 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 234 | 207 | inferred_complete_timeline |
| `Action_None` | 236 | 238 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 105 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 85 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 278 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 299 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 121 | 94 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 147 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 262 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 209 | 182 | inferred_complete_timeline |
| `Action_None` | 212 | 299 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 161 | 134 | inferred_complete_timeline |
| `Action_None` | 165 | 266 | 102 | inferred_complete_timeline |
| `Action_None` | 268 | 299 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 229 | 202 | inferred_complete_timeline |
| `Action_None` | 231 | 299 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 263 | 236 | inferred_complete_timeline |
| `Action_None` | 265 | 270 | 6 | inferred_complete_timeline |
| `Action_None` | 272 | 274 | 3 | inferred_complete_timeline |
| `Action_None` | 276 | 290 | 15 | inferred_complete_timeline |
| `Action_None` | 292 | 299 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–299 | 297 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–45 | 46 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 55–269 | 215 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 59–123 | 19 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 105–265 | 161 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 110–123 | 14 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 111–296 | 156 | 8 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 132–166 | 20 | 3 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 159–259 | 97 | 3 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 162–293 | 118 | 4 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 175–299 | 102 | 7 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 203–245 | 27 | 5 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 236–237 | 2 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 277–299 | 23 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 286–288 | 3 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 290–291 | 2 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 293–299 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `17` (2 segments found)
- ⚠️ `Action_RunBlock` for actor_track_id `18` (C): Annotated start 38 != Inferred start 45
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `9` (7 segments found)
- ⚠️ Ambiguous match for action `Action_FakeHandoff` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 145: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ Row 146: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [28–44], lower_priority='Action_RunBlock' annotated_start=38, effective_Action_RunBlock_start=45.
- ⚠️ Action 'Action_None' range [28-299] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-269] for track '1' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-262] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-234] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-105] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-161] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-266] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-194] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-85] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [38-60] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [71-78] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [83-157] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [159-178] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [180-229] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [231-237] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [240-250] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [51-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-254] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-263] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-270] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-290] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-229] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-278] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-209] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [38-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [59-72] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [45-47] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [38-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [38-196] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [201-246] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [248-256] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-45] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-72] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-76] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-265] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-123] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-196] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-212] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-236] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-255] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-273] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-288] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-296] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-147] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-197] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-254] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-195] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-212] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-253] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-293] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-242] for track '30' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-264] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-289] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-245] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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

</details>