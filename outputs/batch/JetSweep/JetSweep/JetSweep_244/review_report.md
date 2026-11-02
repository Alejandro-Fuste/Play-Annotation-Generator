# Play-Annotation-Generator Annotation Review — JetSweep_244

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_244`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 71
- **Validation Warnings:** 61
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 9
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 47
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | TE1 | offense | `10` | `9` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_LeadBlock` | TE2 | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Toss` | QB | offense | `18` | `17` |
| ⚠️ START CHANGED | `Action_BallCarry` | TE1 | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `10` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 42 |
| ✅ EXACT | `Action_JetMotion` | TE1 | `10` | `9` | 30 | START | 30 | 66 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 43 | START | 43 | 56 |
| ✅ EXACT | `Action_LeadBlock` | TE2 | `8` | `7` | 45 | START | 45 | 80 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `10` | 45 | START | 45 | 98 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `13` | `12` | 45 | START | 45 | 98 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `17` | `16` | 45 | START | 57 | 98 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `2` | 45 | START | 45 | 98 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `6` | `5` | 45 | START | 45 | 98 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 56 | END | 43 | 56 |
| ✅ EXACT | `Action_Toss` | QB | `18` | `17` | 60 | START | 60 | 68 |
| ⚠️ START CHANGED | `Action_BallCarry` | TE1 | `10` | `9` | 69 | START | 101 | 102 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 98 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_SnapReceive` | 43 | 56 | 14 | inferred_complete_timeline |
| `Action_None` | 57 | 59 | 3 | inferred_complete_timeline |
| `Action_Toss` | 60 | 68 | 9 | inferred_complete_timeline |
| `Action_None` | 69 | 100 | 32 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_None` | 108 | 180 | 73 | inferred_complete_timeline |
| `Action_None` | 197 | 239 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 99 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_JetMotion` | 30 | 66 | 37 | inferred_complete_timeline |
| `Action_BallCarry` | 101 | 102 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_LeadBlock` | 45 | 80 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 98 | 54 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 98 | 54 | inferred_complete_timeline |
| `Action_None` | 99 | 99 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_BallSnap` | 43 | 56 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 98 | 42 | inferred_complete_timeline |
| `Action_None` | 99 | 99 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 98 | 54 | inferred_complete_timeline |
| `Action_None` | 99 | 103 | 5 | inferred_complete_timeline |
| `Action_None` | 105 | 108 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 98 | 54 | inferred_complete_timeline |
| `Action_None` | 99 | 102 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 53 | 11 | inferred_complete_timeline |
| `Action_None` | 56 | 74 | 19 | inferred_complete_timeline |
| `Action_None` | 79 | 86 | 8 | inferred_complete_timeline |
| `Action_None` | 90 | 99 | 10 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 104 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 47 | 99 | 53 | inferred_complete_timeline |
| `Action_None` | 104 | 239 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 77 | 35 | inferred_complete_timeline |
| `Action_None` | 79 | 239 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 97 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 94 | 52 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 56 | 14 | inferred_complete_timeline |
| `Action_None` | 60 | 64 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 99 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 93 | 51 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 76–84 | 9 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 86–87 | 2 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 106–216 | 96 | 5 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 106–219 | 105 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 189–239 | 51 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 202–239 | 38 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 233–234 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `17` (C): Annotated start 45 != Inferred start 57
- ⚠️ `Action_BallCarry` for actor_track_id `10` (TE1): Annotated start 69 != Inferred start 101

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 45 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [43–56], lower_priority='Action_ZoneBlock' annotated_start=45, effective_Action_ZoneBlock_start=57.
- ⚠️ Action 'Action_None' range [43-99] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-97] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-56] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-64] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-93] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-102] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-77] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-239] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [45-80] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-99] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [30-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [101-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-98] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '10' starts at frame 99, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [99-99] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-104] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-103] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-99] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-74] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-86] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-99] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 99, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [99-99] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-100] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-84] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-128] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-157] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-177] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-216] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-174] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-219] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '24' has 1 frames without a visible bounding box.
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

</details>