# Play-Annotation-Generator Annotation Review — SplitZone_260

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_260`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 97
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `8` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `3` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 79 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 77 | START | 77 | 88 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `10` | 80 | START | 80 | 191 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `11` | `11` | 80 | START | 89 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `2` | `2` | 80 | START | 80 | 115 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `8` | 80 | START | 80 | 191 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `9` | `9` | 80 | START | 80 | 191 |
| ✅ EXACT | `Action_SplitBlock` | HB | `3` | `3` | 81 | START | 81 | 146 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `5` | 88 | END | 77 | 88 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `5` | 95 | START | 95 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `7` | 103 | START | 103 | 112 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 191 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_SnapReceive` | 77 | 88 | 12 | inferred_complete_timeline |
| `Action_None` | 89 | 94 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 95 | 102 | 8 | inferred_complete_timeline |
| `Action_None` | 103 | 359 | 257 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–334
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_BallCarry` | 103 | 112 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 117 | 311 | 195 | inferred_complete_timeline |
| `Action_BallCarry` | 315 | 322 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 328 | 334 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_SplitBlock` | 81 | 146 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 115 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 191 | 75 | inferred_complete_timeline |
| `Action_None` | 192 | 359 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 191 | 112 | inferred_complete_timeline |
| `Action_None` | 192 | 237 | 46 | inferred_complete_timeline |
| `Action_None` | 239 | 359 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_BallSnap` | 77 | 88 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 191 | 103 | inferred_complete_timeline |
| `Action_None` | 192 | 359 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 191 | 112 | inferred_complete_timeline |
| `Action_None` | 192 | 252 | 61 | inferred_complete_timeline |
| `Action_None` | 254 | 255 | 2 | inferred_complete_timeline |
| `Action_None` | 262 | 359 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 191 | 112 | inferred_complete_timeline |
| `Action_None` | 192 | 359 | 168 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 120 | 44 | inferred_complete_timeline |
| `Action_None` | 124 | 359 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 319 | 243 | inferred_complete_timeline |
| `Action_None` | 322 | 359 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 91 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 151 | 75 | inferred_complete_timeline |
| `Action_None` | 155 | 359 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 101 | 25 | inferred_complete_timeline |
| `Action_None` | 104 | 359 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 359 | 283 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 29–358 | 318 | 4 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 118–359 | 242 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 129–359 | 231 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 140–332 | 187 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 153–359 | 205 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 163–359 | 191 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 168–170 | 3 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 178–251 | 29 | 7 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 212–359 | 148 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 217–359 | 143 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 221–284 | 64 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 262–266 | 5 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 265–267 | 3 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 278–288 | 7 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 282–284 | 3 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 289–307 | 15 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 294–333 | 30 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 295–359 | 65 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 341–357 | 9 | 4 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 354–356 | 3 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `11` (C): Annotated start 80 != Inferred start 89
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (4 segments found)

### Track Identity Issues

- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (LT) duration 112 frames exceeds threshold 90 frames [start=80, end=191].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (RG) duration 112 frames exceeds threshold 90 frames [start=80, end=191].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (LG) duration 112 frames exceeds threshold 90 frames [start=80, end=191].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RT) duration 112 frames exceeds threshold 90 frames [start=80, end=191].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (C) duration 112 frames exceeds threshold 90 frames [start=80, end=191].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [77–88], lower_priority='Action_ZoneBlock' annotated_start=80, effective_Action_ZoneBlock_start=89.
- ⚠️ Action 'Action_None' range [77-319] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-101] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-359] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-115] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [81-146] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-120] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [103-112] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [117-311] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [315-322] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [328-334] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-252] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-359] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-237] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-91] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-151] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-30] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-338] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-358] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-359] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-277] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-332] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-188] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-211] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-224] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-251] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-284] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-266] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-299] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-307] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-300] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-333] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-350] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-356] for track '33' has 1 frames without a visible bounding box.
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

</details>