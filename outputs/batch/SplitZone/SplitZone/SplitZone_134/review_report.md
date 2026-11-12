# Play-Annotation-Generator Annotation Review — SplitZone_134

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_134`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 479
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 134
- **Validation Warnings:** 185
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 120
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | Position_Unknown | Team_Unknown | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `6` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | TE2 | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `15` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 5 | START | 10 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 5 | START | 6 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 5 | START | 6 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 5 | START | 6 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 5 | START | 6 | 18 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `8` | 19 | START | 19 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | Position_Unknown | `13` | `13` | 19 | START | 20 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `12` | `12` | 22 | START | 22 | 61 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `6` | 22 | START | 22 | 39 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `8` | `8` | 22 | START | 31 | 32 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 30 | END | 19 | 30 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 42 | START | 42 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | TE2 | `4` | `4` | 43 | START | 43 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `15` | `15` | 52 | START | 52 | 53 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 84 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 6–155
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 18 | 13 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 30 | 12 | inferred_complete_timeline |
| `Action_None` | 31 | 41 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 42 | 51 | 10 | inferred_complete_timeline |
| `Action_None` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_None` | 67 | 155 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 6–76
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 42 | 37 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 43 | 47 | 5 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 53 | 66 | 14 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 68 | 70 | 3 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 73 | 76 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 10–158
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 21 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 61 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 76 | 5 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_None` | 97 | 158 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 6–39
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 21 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 39 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 6–32
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 18 | 13 | inferred_complete_timeline |
| `Action_BallSnap` | 19 | 30 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 32 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 6–84
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 18 | 13 | inferred_complete_timeline |
| `Action_None` | 19 | 38 | 20 | inferred_complete_timeline |
| `Action_None` | 48 | 59 | 12 | inferred_complete_timeline |
| `Action_None` | 73 | 84 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 6–135
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 18 | 13 | inferred_complete_timeline |
| `Action_None` | 19 | 92 | 74 | inferred_complete_timeline |
| `Action_None` | 95 | 108 | 14 | inferred_complete_timeline |
| `Action_None` | 110 | 118 | 9 | inferred_complete_timeline |
| `Action_None` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 135 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 6–131
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 18 | 13 | inferred_complete_timeline |
| `Action_None` | 19 | 79 | 61 | inferred_complete_timeline |
| `Action_None` | 84 | 131 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 6–146
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 18 | 13 | inferred_complete_timeline |
| `Action_None` | 19 | 75 | 57 | inferred_complete_timeline |
| `Action_None` | 143 | 146 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 6–229
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 18 | 13 | inferred_complete_timeline |
| `Action_None` | 19 | 229 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 6–479
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 18 | 13 | inferred_complete_timeline |
| `Action_None` | 19 | 90 | 72 | inferred_complete_timeline |
| `Action_None` | 97 | 152 | 56 | inferred_complete_timeline |
| `Action_None` | 156 | 160 | 5 | inferred_complete_timeline |
| `Action_None` | 165 | 184 | 20 | inferred_complete_timeline |
| `Action_None` | 187 | 191 | 5 | inferred_complete_timeline |
| `Action_None` | 193 | 479 | 287 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 6–299 | 111 | 6 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 6–127 | 75 | 6 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 20–81 | 30 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 25–190 | 163 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 27–64 | 32 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 37–62 | 13 | 4 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 43–159 | 106 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 55–479 | 393 | 11 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 55–183 | 129 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 96–117 | 22 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 112–479 | 367 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 119–319 | 183 | 5 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 134–151 | 18 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 136–142 | 7 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 214–479 | 259 | 6 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 217–270 | 49 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 235–457 | 217 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 249–479 | 231 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 261–479 | 219 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 267–288 | 21 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 282–422 | 141 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 282–479 | 193 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 286–479 | 194 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 326–479 | 154 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 336–358 | 18 | 4 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 345–346 | 2 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 367–372 | 6 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 396–479 | 84 | 1 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 414–479 | 66 | 1 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 421–479 | 59 | 1 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 424–425 | 2 | 1 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 427–479 | 53 | 1 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 433–434 | 2 | 1 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 443–445 | 3 | 1 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 445–478 | 33 | 2 | Undefined position; Undefined team |
| `46` | `65` | Position_Unknown | Team_Unknown | 449–450 | 2 | 1 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 463–474 | 11 | 2 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 472–473 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `8` (C): Annotated start 22 != Inferred start 31
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `4` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ 38 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 38 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 76 |
| Missing visible bounding boxes during action | 106 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 270: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [19–30], lower_priority='Action_ZoneBlock' annotated_start=22, effective_Action_ZoneBlock_start=31.
- ⚠️ Action 'Action_None' range [19-229] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-75] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-90] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-152] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-184] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-79] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-131] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [43-47] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [53-66] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [68-70] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [73-76] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-108] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-118] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [22-39] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-38] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-59] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-84] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-32] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-41] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-155] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-10] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-56] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-70] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-166] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-290] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-12] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-61] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-90] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-127] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [22-61] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-76] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-158] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [20-27] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [60-81] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-46] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-190] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [52-53] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [60-64] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-40] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-48] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-58] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-58] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-74] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-159] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-63] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-151] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-348] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-364] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-384] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-396] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-405] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-430] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-442] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-117] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-211] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-170] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-243] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-251] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-319] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-151] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-142] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-348] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-384] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-388] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-393] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-397] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-263] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-300] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-451] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-457] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-285] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-422] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-416] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-338] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-344] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-355] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-372] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-425] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-434] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-445] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-458] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-478] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-450] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-469] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-474] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-473] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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