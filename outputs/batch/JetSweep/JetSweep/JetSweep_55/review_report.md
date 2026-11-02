# Play-Annotation-Generator Annotation Review — JetSweep_55

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_55`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 63
- **Validation Warnings:** 60
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 39
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `22` | `19` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE2 | offense | `4` | `3` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Toss` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `22` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `5` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 33 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `22` | `19` | 26 | START | 26 | 62 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 34 | START | 34 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE2 | `4` | `3` | 36 | START | 36 | 73 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `12` | `11` | 36 | START | 46 | 94 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `14` | `13` | 36 | START | 36 | 94 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `3` | `2` | 36 | START | 36 | 94 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `5` | 36 | START | 36 | 90 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 45 | END | 34 | 45 |
| ✅ EXACT | `Action_Toss` | QB | `10` | `9` | 55 | START | 55 | 62 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `22` | `19` | 63 | START | 63 | 182 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 94 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_SnapReceive` | 34 | 45 | 12 | inferred_complete_timeline |
| `Action_None` | 46 | 54 | 9 | inferred_complete_timeline |
| `Action_Toss` | 55 | 62 | 8 | inferred_complete_timeline |
| `Action_None` | 63 | 121 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 97 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 81 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_LeadBlock` | 36 | 73 | 38 | inferred_complete_timeline |
| `Action_LeadBlock` | 80 | 94 | 15 | inferred_complete_timeline |
| `Action_None` | 95 | 145 | 51 | inferred_complete_timeline |
| `Action_None` | 148 | 210 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 90 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 94 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_BallSnap` | 34 | 45 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 94 | 49 | inferred_complete_timeline |
| `Action_None` | 95 | 95 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 94 | 59 | inferred_complete_timeline |
| `Action_None` | 95 | 210 | 116 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 51 | 18 | inferred_complete_timeline |
| `Action_None` | 53 | 85 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 33 | 27 | inferred_complete_timeline |
| `Action_None` | 34 | 210 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 68 | 35 | inferred_complete_timeline |
| `Action_None` | 93 | 96 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 210 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 196 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 33 | 15 | inferred_complete_timeline |
| `Action_None` | 34 | 101 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 61 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 113 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 13 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 33 | 13 | inferred_complete_timeline |
| `Action_None` | 34 | 52 | 19 | inferred_complete_timeline |
| `Action_None` | 56 | 207 | 152 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 4–7 | 4 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 19–65 | 36 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 25–182 | 158 | 3 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 79–80 | 2 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 87–210 | 124 | 1 | Undefined position; Undefined team |
| `22` | `34` | Position_Unknown | Team_Unknown | 92–210 | 119 | 1 | Undefined position; Undefined team |
| `23` | `36` | Position_Unknown | Team_Unknown | 101–210 | 110 | 1 | Undefined position; Undefined team |
| `24` | `41` | Position_Unknown | Team_Unknown | 163–210 | 48 | 1 | Undefined position; Undefined team |
| `25` | `42` | Position_Unknown | Team_Unknown | 163–210 | 48 | 1 | Undefined position; Undefined team |
| `26` | `45` | Position_Unknown | Team_Unknown | 195–210 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `4` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `12` (C): Annotated start 36 != Inferred start 46

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 38 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [34–45], lower_priority='Action_ZoneBlock' annotated_start=36, effective_Action_ZoneBlock_start=46.
- ⚠️ Action 'Action_None' range [34-61] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-113] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [36-73] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-145] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-81] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [36-90] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-196] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-97] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-121] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-101] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 95, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [95-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-51] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [36-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-68] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-96] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-13] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-207] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-7] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-22] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-65] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [63-182] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-210] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '26' has 1 frames without a visible bounding box.
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

</details>