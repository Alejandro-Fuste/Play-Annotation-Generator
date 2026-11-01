# Play-Annotation-Generator Annotation Review — InsideZoneRead_62

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_62`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 509
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 8
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 73 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `8` | 74 | START | 74 | 87 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `0` | 76 | START | 76 | 173 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `11` | `10` | 76 | START | 76 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `4` | `3` | 76 | START | 76 | 173 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `4` | 76 | START | 76 | 173 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `9` | `8` | 76 | START | 88 | 173 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 87 | END | 74 | 87 |
| ✅ EXACT | `Action_ReadDefender` | QB | `6` | `5` | 92 | START | 92 | 101 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `5` | 102 | START | 102 | 110 |
| ✅ EXACT | `Action_BallCarry` | RB | `3` | `2` | 111 | START | 111 | 509 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 173 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 503

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_SnapReceive` | 74 | 87 | 14 | inferred_complete_timeline |
| `Action_None` | 88 | 91 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 92 | 101 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 102 | 110 | 9 | inferred_complete_timeline |
| `Action_None` | 111 | 178 | 68 | inferred_complete_timeline |
| `Action_None` | 186 | 509 | 324 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_BallCarry` | 111 | 509 | 399 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 173 | 98 | inferred_complete_timeline |
| `Action_None` | 174 | 509 | 336 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 173 | 98 | inferred_complete_timeline |
| `Action_None` | 174 | 509 | 336 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_BallSnap` | 74 | 87 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 173 | 86 | inferred_complete_timeline |
| `Action_None` | 174 | 509 | 336 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 508

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 173 | 98 | inferred_complete_timeline |
| `Action_None` | 174 | 192 | 19 | inferred_complete_timeline |
| `Action_None` | 195 | 509 | 315 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 173 | 98 | inferred_complete_timeline |
| `Action_None` | 174 | 509 | 336 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 499

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 110 | 37 | inferred_complete_timeline |
| `Action_None` | 116 | 142 | 27 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 148 | 165 | 18 | inferred_complete_timeline |
| `Action_None` | 169 | 509 | 341 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 500

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 197 | 124 | inferred_complete_timeline |
| `Action_None` | 200 | 203 | 4 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_None` | 214 | 509 | 296 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 84 | 11 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 502

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 105 | 32 | inferred_complete_timeline |
| `Action_None` | 114 | 509 | 396 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 170 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 150 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 145 | 72 | inferred_complete_timeline |
| `Action_None` | 148 | 175 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 3–501 | 476 | 5 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 88–509 | 418 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 172–186 | 15 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 178–441 | 264 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 181–269 | 80 | 4 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 202–509 | 308 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 225–509 | 275 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 231–252 | 20 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 257–258 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 258–508 | 235 | 5 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 279–509 | 231 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 288–509 | 178 | 8 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 308–509 | 201 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 328–509 | 182 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 339–359 | 10 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 445–499 | 49 | 3 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 463–464 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `9` (C): Annotated start 76 != Inferred start 88

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '0' (LT) duration 98 frames exceeds threshold 90 frames [start=76, end=173].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (LG) duration 98 frames exceeds threshold 90 frames [start=76, end=173].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (RT) duration 98 frames exceeds threshold 90 frames [start=76, end=173].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (C) duration 98 frames exceeds threshold 90 frames [start=76, end=173].
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [74–87], lower_priority='Action_ZoneBlock' annotated_start=76, effective_Action_ZoneBlock_start=88.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RG) duration 98 frames exceeds threshold 90 frames [start=76, end=173].
- ⚠️ Action 'Action_None' range [74-150] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-178] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-197] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-170] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-84] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-192] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-110] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-165] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-145] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-105] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-509] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-492] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-501] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-92] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-509] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-186] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-441] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-249] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-263] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-336] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-488] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-509] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-246] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-332] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-351] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-486] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-508] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-389] for track '26' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-413] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-455] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-463] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-466] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-481] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-363] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-342] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-359] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-487] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-493] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-499] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-464] for track '31' has 1 frames without a visible bounding box.
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

</details>