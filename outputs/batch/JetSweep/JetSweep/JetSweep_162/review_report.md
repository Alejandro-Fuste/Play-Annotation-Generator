# Play-Annotation-Generator Annotation Review — JetSweep_162

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_162`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 92
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
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `19` | `18` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `18` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `16` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `17` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 76 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `19` | `18` | 57 | START | 57 | 105 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 77 | START | 77 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | `14` | `13` | 79 | START | 79 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `10` | `9` | 79 | START | 79 | 143 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `10` | 79 | START | 79 | 143 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `13` | `12` | 79 | START | 93 | 143 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `15` | `14` | 79 | START | 79 | 143 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `18` | `17` | 79 | START | 79 | 143 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 92 | END | 77 | 92 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 99 | START | 99 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `19` | `18` | 106 | START | 106 | 144 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 143 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_SnapReceive` | 77 | 92 | 16 | inferred_complete_timeline |
| `Action_None` | 93 | 98 | 6 | inferred_complete_timeline |
| `Action_Toss` | 99 | 105 | 7 | inferred_complete_timeline |
| `Action_None` | 106 | 154 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_LeadBlock` | 79 | 92 | 14 | inferred_complete_timeline |
| `Action_LeadBlock` | 94 | 143 | 50 | inferred_complete_timeline |
| `Action_None` | 144 | 158 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 146 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 154 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 143 | 65 | inferred_complete_timeline |
| `Action_None` | 144 | 155 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 143 | 65 | inferred_complete_timeline |
| `Action_None` | 144 | 154 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_BallSnap` | 77 | 92 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 143 | 51 | inferred_complete_timeline |
| `Action_None` | 144 | 160 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 143 | 65 | inferred_complete_timeline |
| `Action_None` | 144 | 154 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 143 | 65 | inferred_complete_timeline |
| `Action_None` | 144 | 173 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 160 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 154 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 154 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 154 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 143 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 135 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 154 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 154 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 120 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 56–269 | 200 | 6 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 88–92 | 5 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 113–115 | 3 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 138–140 | 3 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 155–171 | 17 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 155–162 | 8 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 155–269 | 114 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 155–160 | 6 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 155–157 | 3 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 155–193 | 39 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 158–175 | 18 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 162–269 | 106 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 166–269 | 104 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 169–269 | 100 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 185–220 | 34 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 195–196 | 2 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 205–207 | 3 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 209–212 | 4 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 220–269 | 6 | 2 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 227–269 | 43 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 233–234 | 2 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `13` (C): Annotated start 79 != Inferred start 93
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [77–92], lower_priority='Action_ZoneBlock' annotated_start=79, effective_Action_ZoneBlock_start=93.
- ⚠️ Action 'Action_None' range [77-135] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-143] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-154] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-154] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-154] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-154] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-154] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-155] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-154] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-160] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [79-92] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [94-143] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-158] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-154] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-154] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-146] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-173] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [106-144] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [156-232] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [234-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [242-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-92] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-171] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-162] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-243] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-160] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-193] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-175] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-217] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-229] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-216] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-269] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '38' has 1 frames without a visible bounding box.
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

</details>