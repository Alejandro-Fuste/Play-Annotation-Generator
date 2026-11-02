# Play-Annotation-Generator Annotation Review — JetSweep_61

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_61`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 127
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `22` | `18` |
| ⚠️ START CHANGED | `Action_BallSnap` | C | offense | `19` | `17` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `14` | `13` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `19` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `6` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `19` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `22` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `1` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 8 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 20 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `22` | `18` | 18 | START | 18 | 47 |
| ⚠️ START CHANGED | `Action_BallSnap` | C | `19` | `17` | 21 | START | 24 | 37 |
| ✅ EXACT | `Action_LeadBlock` | RB | `2` | `1` | 27 | START | 27 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `10` | `9` | 27 | START | 27 | 77 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `10` | 27 | START | 27 | 77 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `14` | `13` | 27 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `19` | `17` | 27 | START | 38 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `6` | `5` | 27 | START | 27 | 77 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `6` | 27 | START | 27 | 68 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 37 | END | 21 | 37 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 42 | START | 42 | 48 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `19` | `17` | 47 | START | 47 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `22` | `18` | 49 | START | 49 | 197 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 77 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 37 | 17 | inferred_complete_timeline |
| `Action_None` | 38 | 41 | 4 | inferred_complete_timeline |
| `Action_Toss` | 42 | 48 | 7 | inferred_complete_timeline |
| `Action_None` | 49 | 86 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_LeadBlock` | 27 | 77 | 51 | inferred_complete_timeline |
| `Action_None` | 78 | 269 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 54 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 60 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 77 | 51 | inferred_complete_timeline |
| `Action_None` | 78 | 176 | 99 | inferred_complete_timeline |
| `Action_None` | 178 | 241 | 64 | inferred_complete_timeline |
| `Action_None` | 245 | 253 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 77 | 51 | inferred_complete_timeline |
| `Action_None` | 78 | 119 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 8–190
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 10 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 24 | 37 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 46 | 9 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 47 | 77 | 31 | inferred_complete_timeline |
| `Action_None` | 78 | 190 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 77 | 51 | inferred_complete_timeline |
| `Action_None` | 78 | 78 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–19
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 68 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 244 | 224 | inferred_complete_timeline |
| `Action_None` | 260 | 269 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 77 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–39
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 39 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 61 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 51 | 31 | inferred_complete_timeline |
| `Action_None` | 72 | 269 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 132 | 112 | inferred_complete_timeline |
| `Action_None` | 134 | 141 | 8 | inferred_complete_timeline |
| `Action_None` | 143 | 153 | 11 | inferred_complete_timeline |
| `Action_None` | 163 | 169 | 7 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_None` | 177 | 185 | 9 | inferred_complete_timeline |
| `Action_None` | 188 | 196 | 9 | inferred_complete_timeline |
| `Action_None` | 199 | 224 | 26 | inferred_complete_timeline |
| `Action_None` | 226 | 269 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 119 | 99 | inferred_complete_timeline |
| `Action_None` | 123 | 188 | 66 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 210 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–61 | 62 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 18–202 | 183 | 3 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 25–197 | 163 | 3 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 43–261 | 219 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 80–269 | 188 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 82–207 | 113 | 3 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 90–269 | 180 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 95–128 | 30 | 3 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 106–269 | 164 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 153–170 | 18 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 170–182 | 13 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 183–185 | 3 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 199–263 | 42 | 5 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 208–252 | 39 | 3 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 216–269 | 42 | 4 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 217–238 | 7 | 2 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 220–269 | 50 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 221–269 | 49 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 230–237 | 7 | 2 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 248–269 | 22 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 252–262 | 11 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 253–269 | 17 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 255–269 | 15 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 259–269 | 11 | 1 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 259–268 | 9 | 2 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `19` (C): Annotated start 21 != Inferred start 24
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `14` (RG)
- ⚠️ `Action_ZoneBlock` for actor_track_id `19` (C): Annotated start 27 != Inferred start 38
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 124: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ Row 124: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 124: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '13' has invalid range: start=27, end=19. Clamping end to start.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [21–37], lower_priority='Action_ZoneBlock' annotated_start=27, effective_Action_ZoneBlock_start=38.
- ⚠️ Action 'Action_None' range [21-54] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-269] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-132] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-141] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-153] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-169] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-185] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-196] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-224] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-60] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-61] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '5' starts at frame 78, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [78-78] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [27-68] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-86] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-119] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-188] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-176] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-253] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-119] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-51] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-61] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-244] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-39] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-10] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [24-37] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-190] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [18-47] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [49-197] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [199-202] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-34] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-188] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-261] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-118] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-207] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-113] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-122] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-170] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-182] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-215] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-233] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-251] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-263] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-221] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-252] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-221] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-234] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-262] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-265] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>