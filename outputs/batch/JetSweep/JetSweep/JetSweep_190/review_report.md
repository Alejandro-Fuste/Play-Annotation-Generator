# Play-Annotation-Generator Annotation Review — JetSweep_190

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_190`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 134
- **Validation Warnings:** 167
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 110
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `9` | `8` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 10 |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | `17` | `16` | 2 | START | 3 | 36 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 10 | START | 10 | 23 |
| ✅ EXACT | `Action_LeadBlock` | TE | `9` | `8` | 11 | START | 11 | 96 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `12` | `11` | 11 | START | 11 | 56 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `15` | `14` | 11 | START | 24 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `2` | 11 | START | 11 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `7` | `6` | 11 | START | 11 | 51 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `7` | 11 | START | 11 | 53 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 23 | END | 10 | 23 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 35 | START | 35 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `17` | `16` | 37 | START | 37 | 244 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 96 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–71
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 23 | 14 | inferred_complete_timeline |
| `Action_None` | 24 | 34 | 11 | inferred_complete_timeline |
| `Action_Toss` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_None` | 37 | 50 | 14 | inferred_complete_timeline |
| `Action_None` | 52 | 71 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 65 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_LeadBlock` | 11 | 96 | 86 | inferred_complete_timeline |
| `Action_None` | 97 | 129 | 33 | inferred_complete_timeline |
| `Action_None` | 131 | 269 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 56 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 49 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 59 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 23 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 61 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 51 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 64 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 53 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 50 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 269 | 260 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–45
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 45 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–49
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 31 | 22 | inferred_complete_timeline |
| `Action_None` | 35 | 49 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 58 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 216 | 207 | inferred_complete_timeline |
| `Action_None` | 218 | 224 | 7 | inferred_complete_timeline |
| `Action_None` | 227 | 236 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 128 | 119 | inferred_complete_timeline |
| `Action_None` | 131 | 135 | 5 | inferred_complete_timeline |
| `Action_None` | 137 | 269 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 57 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 3–269 | 261 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 6–269 | 252 | 5 | Undefined position; Undefined team |
| `18` | `26` | Position_Unknown | Team_Unknown | 86–88 | 3 | 1 | Undefined position; Undefined team |
| `19` | `27` | Position_Unknown | Team_Unknown | 100–269 | 165 | 2 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 116–269 | 154 | 1 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 140–268 | 78 | 5 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 144–240 | 55 | 5 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 150–174 | 25 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 151–269 | 111 | 2 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 151–164 | 14 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 157–260 | 59 | 6 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 158–269 | 112 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 159–269 | 108 | 3 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 159–183 | 24 | 2 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 165–269 | 104 | 2 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 165–172 | 7 | 2 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 168–269 | 84 | 4 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 168–205 | 38 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 172–269 | 98 | 1 | Undefined position; Undefined team |
| `35` | `55` | Position_Unknown | Team_Unknown | 179–268 | 59 | 9 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 186–211 | 13 | 3 | Undefined position; Undefined team |
| `37` | `60` | Position_Unknown | Team_Unknown | 196–268 | 47 | 3 | Undefined position; Undefined team |
| `38` | `61` | Position_Unknown | Team_Unknown | 196–258 | 35 | 5 | Undefined position; Undefined team |
| `39` | `63` | Position_Unknown | Team_Unknown | 203–269 | 65 | 2 | Undefined position; Undefined team |
| `40` | `64` | Position_Unknown | Team_Unknown | 210–268 | 4 | 2 | Undefined position; Undefined team |
| `41` | `65` | Position_Unknown | Team_Unknown | 217–222 | 6 | 1 | Undefined position; Undefined team |
| `42` | `66` | Position_Unknown | Team_Unknown | 219–263 | 40 | 3 | Undefined position; Undefined team |
| `43` | `67` | Position_Unknown | Team_Unknown | 233–269 | 37 | 1 | Undefined position; Undefined team |
| `44` | `68` | Position_Unknown | Team_Unknown | 238–269 | 13 | 4 | Undefined position; Undefined team |
| `45` | `69` | Position_Unknown | Team_Unknown | 241–268 | 24 | 3 | Undefined position; Undefined team |
| `46` | `70` | Position_Unknown | Team_Unknown | 246–269 | 17 | 2 | Undefined position; Undefined team |
| `47` | `71` | Position_Unknown | Team_Unknown | 250–251 | 2 | 1 | Undefined position; Undefined team |
| `48` | `72` | Position_Unknown | Team_Unknown | 264–269 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_JetMotion` for actor_track_id `17` (Position_Unknown): Annotated start 2 != Inferred start 3
- ⚠️ `Action_ZoneBlock` for actor_track_id `15` (C): Annotated start 11 != Inferred start 24
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 99 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [10–23], lower_priority='Action_ZoneBlock' annotated_start=11, effective_Action_ZoneBlock_start=24.
- ⚠️ Action 'Action_None' range [10-216] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-224] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-236] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-58] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-49] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [57-59] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-50] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-65] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-128] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-51] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [53-64] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-53] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-129] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-57] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-50] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-71] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-56] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-31] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-49] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [24-61] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-45] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [37-244] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-51] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-238] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-207] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-268] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-206] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-224] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-174] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-183] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-164] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-183] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-206] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-213] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-269] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-164] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-183] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-172] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-269] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-218] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-269] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-205] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-198] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-207] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-216] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-227] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-237] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-190] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-230] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-259] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-224] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-258] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-222] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-246] for track '42' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-253] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-263] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-246] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-265] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-252] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.

</details>