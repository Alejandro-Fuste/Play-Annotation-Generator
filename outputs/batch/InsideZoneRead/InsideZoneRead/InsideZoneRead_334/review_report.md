# Play-Annotation-Generator Annotation Review — InsideZoneRead_334

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_334`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `21` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | TE2 | offense | `5` | `4` |
| ✅ EXACT | `Action_ReadDefender` | TE2 | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LB2 | defense | `1` | `0` |
| ✅ EXACT | `Action_Keep` | TE2 | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | TE2 | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 2 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 2 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 2 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 2 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 2 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 2 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `2` | `Group` | 2 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 2 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `5` | `Group` | 2 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 2 | START | 0 | 31 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `21` | `19` | 29 | START | 35 | 40 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `9` | 32 | START | 32 | 110 |
| ✅ EXACT | `Action_ZoneBlock` | C | `12` | `11` | 32 | START | 32 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `14` | `13` | 32 | START | 32 | 59 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `16` | `15` | 32 | START | 32 | 100 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `6` | `5` | 32 | START | 32 | 104 |
| ✅ EXACT | `Action_SnapReceive` | TE2 | `5` | `4` | 40 | END | 29 | 40 |
| ✅ EXACT | `Action_ReadDefender` | TE2 | `5` | `4` | 47 | START | 47 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LB2 | `1` | `0` | 48 | START | 48 | 76 |
| ✅ EXACT | `Action_Keep` | TE2 | `5` | `4` | 62 | START | 62 | 75 |
| ✅ EXACT | `Action_BallCarry` | TE2 | `5` | `4` | 76 | START | 76 | 158 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 110 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 134 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 94 | 66 | inferred_complete_timeline |
| `Action_None` | 100 | 116 | 17 | inferred_complete_timeline |
| `Action_None` | 128 | 130 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 53 | 25 | inferred_complete_timeline |
| `Action_None` | 56 | 107 | 52 | inferred_complete_timeline |
| `Action_None` | 109 | 165 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_SnapReceive` | 29 | 40 | 12 | inferred_complete_timeline |
| `Action_None` | 41 | 46 | 6 | inferred_complete_timeline |
| `Action_ReadDefender` | 47 | 61 | 15 | inferred_complete_timeline |
| `Action_Keep` | 62 | 75 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 76 | 158 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 145 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 59 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 110 | 49 | inferred_complete_timeline |
| `Action_None` | 111 | 117 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 100 | 69 | inferred_complete_timeline |
| `Action_None` | 117 | 119 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 110 | 79 | inferred_complete_timeline |
| `Action_None` | 111 | 113 | 3 | inferred_complete_timeline |
| `Action_None` | 119 | 163 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 104 | 73 | inferred_complete_timeline |
| `Action_None` | 120 | 161 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 110 | 79 | inferred_complete_timeline |
| `Action_None` | 111 | 142 | 32 | inferred_complete_timeline |
| `Action_None` | 150 | 159 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 61 | 33 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_None` | 114 | 239 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 81 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 66 | 38 | inferred_complete_timeline |
| `Action_None` | 70 | 81 | 12 | inferred_complete_timeline |
| `Action_None` | 83 | 124 | 42 | inferred_complete_timeline |
| `Action_None` | 131 | 157 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 177 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 48 | 76 | 29 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 78 | 88 | 11 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 95 | 106 | 12 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 109 | 110 | 2 | inferred_complete_timeline |
| `Action_None` | 111 | 114 | 4 | inferred_complete_timeline |
| `Action_None` | 116 | 120 | 5 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 160 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 156 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–22
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 135 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 154 | 126 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `21` | Position_Unknown | Team_Unknown | 35–113 | 76 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 35–108 | 71 | 3 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 108–152 | 34 | 3 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 127–128 | 2 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 128–158 | 29 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 133–152 | 8 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 154–239 | 86 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 159–239 | 80 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 164–239 | 62 | 3 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 220–221 | 2 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 223–224 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `21` (Position_Unknown): Annotated start 29 != Inferred start 35
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `1` (4 segments found)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 57 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_BlockSecondLevel' range [48-76] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [78-88] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [95-106] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-160] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-145] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-94] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-116] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-156] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [76-158] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-104] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-161] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-154] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-177] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-135] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-142] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-159] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-53] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-107] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-165] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-110] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-163] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-66] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-81] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-124] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-157] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-59] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-117] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-134] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-100] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-61] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-65] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-72] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-108] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-152] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-151] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-158] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-152] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-229] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-217] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '29' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_334'; source metadata written as null.

</details>