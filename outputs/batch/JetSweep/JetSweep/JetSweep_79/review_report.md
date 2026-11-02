# Play-Annotation-Generator Annotation Review — JetSweep_79

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_79`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 9
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `19` | `18` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `2` | `1` |
| ✅ EXACT | `Action_SealBlock` | TE2 | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Toss` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `19` | `18` | 17 | START | 17 | 49 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 24 | START | 24 | 38 |
| ✅ EXACT | `Action_LeadBlock` | RB | `2` | `1` | 25 | START | 25 | 82 |
| ✅ EXACT | `Action_SealBlock` | TE2 | `4` | `3` | 25 | START | 25 | 72 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `0` | 25 | START | 25 | 66 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `11` | `10` | 25 | START | 25 | 82 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `18` | `17` | 25 | START | 39 | 77 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `5` | 25 | START | 25 | 76 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `8` | 25 | START | 25 | 81 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 38 | END | 24 | 38 |
| ✅ EXACT | `Action_Toss` | QB | `5` | `4` | 41 | START | 41 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `19` | `18` | 55 | START | 55 | 140 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 82 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_SnapReceive` | 24 | 38 | 15 | inferred_complete_timeline |
| `Action_None` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_Toss` | 41 | 54 | 14 | inferred_complete_timeline |
| `Action_None` | 55 | 76 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_LeadBlock` | 25 | 82 | 58 | inferred_complete_timeline |
| `Action_None` | 83 | 210 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 106 | 83 | inferred_complete_timeline |
| `Action_None` | 109 | 146 | 38 | inferred_complete_timeline |
| `Action_None` | 148 | 210 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_SealBlock` | 25 | 72 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 66 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 76 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_BallSnap` | 24 | 38 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 77 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 81 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 82 | 58 | inferred_complete_timeline |
| `Action_None` | 83 | 210 | 128 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 73 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 74 | 51 | inferred_complete_timeline |
| `Action_None` | 77 | 137 | 61 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–34
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 34 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–29
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 29 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 104 | 81 | inferred_complete_timeline |
| `Action_None` | 106 | 108 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 132 | 109 | inferred_complete_timeline |
| `Action_None` | 144 | 173 | 30 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 50 | 27 | inferred_complete_timeline |
| `Action_None` | 57 | 58 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 89 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 58 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 17–191 | 167 | 6 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 59–79 | 21 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 62–73 | 12 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 72–149 | 78 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 73–86 | 5 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 74–209 | 129 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 83–210 | 128 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 103–194 | 74 | 5 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 129–130 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 131–199 | 61 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 159–163 | 5 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 160–210 | 50 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 162–164 | 3 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 170–179 | 10 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 182–210 | 29 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 190–196 | 7 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 204–210 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `19` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `18` (C): Annotated start 25 != Inferred start 39
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [24–38], lower_priority='Action_ZoneBlock' annotated_start=25, effective_Action_ZoneBlock_start=39.
- ⚠️ Action 'Action_ZoneBlock' range [25-66] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-132] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-173] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [25-72] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-76] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-76] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-50] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-104] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-81] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-58] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-89] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-73] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-74] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-137] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-146] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-34] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-29] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-77] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [17-49] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [55-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [142-144] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [150-154] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [156-191] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-79] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-73] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-110] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-182] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-197] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-209] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-119] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-173] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-199] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-163] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-200] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-179] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-196] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '34' has 1 frames without a visible bounding box.
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