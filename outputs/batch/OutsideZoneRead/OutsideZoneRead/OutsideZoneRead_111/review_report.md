# Play-Annotation-Generator Annotation Review — OutsideZoneRead_111

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_111`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 91
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
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Keep` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `7` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 1 | START | 1 | 11 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `9` | 4 | START | 4 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `16` | 4 | START | 12 | 18 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `19` | `18` | 4 | START | 4 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 4 | START | 4 | 79 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `22` | `21` | 4 | START | 4 | 79 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 11 | END | 1 | 11 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `15` | `14` | 14 | START | 14 | 15 |
| ✅ EXACT | `Action_Keep` | QB | `15` | `14` | 16 | START | 16 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `15` | `14` | 57 | START | 57 | 298 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 79 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–309
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 11 | 11 | inferred_complete_timeline |
| `Action_None` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 14 | 15 | 2 | inferred_complete_timeline |
| `Action_Keep` | 16 | 56 | 41 | inferred_complete_timeline |
| `Action_BallCarry` | 57 | 298 | 242 | inferred_complete_timeline |
| `Action_BallCarry` | 300 | 301 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 308 | 309 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 329 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 329 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 329 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 329 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 134 | 134 | inferred_complete_timeline |
| `Action_None` | 141 | 329 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 79 | 76 | inferred_complete_timeline |
| `Action_None` | 80 | 289 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 79 | 76 | inferred_complete_timeline |
| `Action_None` | 80 | 274 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–23
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 11 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 12 | 18 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 23 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 79 | 76 | inferred_complete_timeline |
| `Action_None` | 80 | 328 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–324
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 79 | 76 | inferred_complete_timeline |
| `Action_None` | 80 | 324 | 245 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–34
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 34 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–290
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 90 | 90 | inferred_complete_timeline |
| `Action_None` | 101 | 290 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 24 | 24 | inferred_complete_timeline |
| `Action_None` | 29 | 55 | 27 | inferred_complete_timeline |
| `Action_None` | 57 | 329 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 30 | 30 | inferred_complete_timeline |
| `Action_None` | 34 | 65 | 32 | inferred_complete_timeline |
| `Action_None` | 70 | 88 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 137 | 137 | inferred_complete_timeline |
| `Action_None` | 220 | 221 | 2 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–301
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 75 | 75 | inferred_complete_timeline |
| `Action_None` | 82 | 301 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–318
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 318 | 318 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 329 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 329 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 329 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 329 | 329 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 45–329 | 285 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 59–133 | 72 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 67–68 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 82–313 | 226 | 4 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 83–304 | 222 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 114–313 | 192 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 116–160 | 32 | 4 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 122–126 | 5 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 141–329 | 189 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 167–211 | 26 | 5 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 223–272 | 10 | 4 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 257–263 | 5 | 2 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 268–305 | 30 | 5 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 287–289 | 3 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 309–317 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [1–11], lower_priority='Action_ZoneBlock' annotated_start=4, effective_Action_ZoneBlock_start=12.
- ⚠️ Action 'Action_None' range [1-137] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-134] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-318] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-90] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-290] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-79] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-324] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-24] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-75] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-301] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [57-298] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [300-301] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [308-309] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-30] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [12-18] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [22-23] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-34] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-328] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-274] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-289] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-113] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-133] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-168] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-202] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-313] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-304] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-313] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-129] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-139] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-172] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-194] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-206] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-278] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-302] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-289] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-317] for track '36' has 2 frames without a visible bounding box.
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