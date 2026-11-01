# Play-Annotation-Generator Annotation Review — InsideZoneRead_220

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_220`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 122
- **Validation Warnings:** 116
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | CB5 | defense | `18` | `17` |
| ✅ EXACT | `Action_ReadDefender` | CB5 | defense | `18` | `17` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `19` | `18` |
| ✅ EXACT | `Action_Handoff` | CB5 | defense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `22` | `21` | 109 | START | 109 | 119 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `12` | `11` | 112 | START | 112 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 112 | START | 112 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `19` | 112 | START | 112 | 197 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `21` | `20` | 112 | START | 112 | 124 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `22` | `21` | 112 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | CB5 | `18` | `17` | 125 | END | 109 | 125 |
| ✅ EXACT | `Action_ReadDefender` | CB5 | `18` | `17` | 129 | START | 129 | 143 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `19` | `18` | 141 | START | 141 | 197 |
| ✅ EXACT | `Action_Handoff` | CB5 | `18` | `17` | 144 | START | 144 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `10` | `9` | 151 | START | 151 | 181 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 197 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 189 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 224 | 116 | inferred_complete_timeline |
| `Action_None` | 227 | 329 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 219 | 111 | inferred_complete_timeline |
| `Action_None` | 222 | 234 | 13 | inferred_complete_timeline |
| `Action_None` | 237 | 272 | 36 | inferred_complete_timeline |
| `Action_None` | 274 | 329 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 275 | 167 | inferred_complete_timeline |
| `Action_None` | 285 | 329 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 197 | 86 | inferred_complete_timeline |
| `Action_None` | 198 | 329 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 140 | 29 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 141 | 197 | 57 | inferred_complete_timeline |
| `Action_None` | 198 | 263 | 66 | inferred_complete_timeline |
| `Action_None` | 265 | 272 | 8 | inferred_complete_timeline |
| `Action_None` | 283 | 291 | 9 | inferred_complete_timeline |
| `Action_None` | 294 | 329 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_BallSnap` | 109 | 119 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 124 | 125 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 124 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 197 | 86 | inferred_complete_timeline |
| `Action_None` | 198 | 329 | 132 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 131 | 23 | inferred_complete_timeline |
| `Action_None` | 136 | 138 | 3 | inferred_complete_timeline |
| `Action_None` | 140 | 329 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 329 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 164 | 56 | inferred_complete_timeline |
| `Action_None` | 166 | 191 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–305
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 261 | 153 | inferred_complete_timeline |
| `Action_None` | 263 | 266 | 4 | inferred_complete_timeline |
| `Action_None` | 272 | 275 | 4 | inferred_complete_timeline |
| `Action_None` | 281 | 282 | 2 | inferred_complete_timeline |
| `Action_None` | 285 | 305 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 166 | 58 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 164 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–322
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 278 | 170 | inferred_complete_timeline |
| `Action_None` | 281 | 282 | 2 | inferred_complete_timeline |
| `Action_None` | 284 | 322 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 184 | 76 | inferred_complete_timeline |
| `Action_None` | 188 | 252 | 65 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 329 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 329 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_SnapReceive` | 109 | 125 | 17 | inferred_complete_timeline |
| `Action_None` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 129 | 143 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 144 | 150 | 7 | inferred_complete_timeline |
| `Action_None` | 151 | 329 | 179 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–303 | 221 | 4 | Undefined position; Undefined team |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–185 | 185 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 13–19 | 4 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 82–329 | 230 | 7 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 147–256 | 71 | 7 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 147–148 | 2 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 173–329 | 154 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 189–329 | 111 | 5 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 190–329 | 130 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 192–263 | 66 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 197–260 | 64 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 203–303 | 99 | 3 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 228–229 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 230–329 | 100 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 266–323 | 38 | 3 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 269–329 | 59 | 2 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 276–283 | 6 | 2 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 292–320 | 21 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `22` (C)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 440: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ Row 440: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [109–125], lower_priority='Action_ZoneBlock' annotated_start=112, effective_Action_ZoneBlock_start=126.
- ⚠️ Action 'Action_None' range [109-275] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-131] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-219] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-234] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-272] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-189] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-278] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-322] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-196] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-225] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-224] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [151-181] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [183-185] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-166] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-164] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-191] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-164] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-184] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-252] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-261] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-266] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-305] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-263] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-272] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-291] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-197] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-124] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [109-119] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [124-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-14] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-19] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-85] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-129] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-252] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-189] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-209] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-256] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-178] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-229] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-224] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-242] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-194] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-304] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-252] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-263] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-260] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-300] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-293] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-323] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-273] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-320] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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