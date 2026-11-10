# Play-Annotation-Generator Annotation Review — RPO_158

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_158`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `0` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | RG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBall` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `0` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `10` | `10` | 45 | START | 45 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `13` | `13` | 45 | START | 45 | 54 |
| ❌ MISSING SEGMENT | `Action_RunBlock` | RG | `16` | `16` | 45 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `4` | `4` | 45 | START | 45 | 53 |
| ✅ EXACT | `Action_RunBlock` | LT | `8` | `8` | 45 | START | 45 | 90 |
| ✅ EXACT | `Action_ReadDefender` | QB | `9` | `9` | 54 | START | 54 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBall` | QB | `9` | `9` | 68 | START | 68 | 70 |
| ✅ EXACT | `Action_ThrowPass` | QB | `9` | `9` | 83 | START | 83 | 90 |

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
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 53 | 10 | inferred_complete_timeline |
| `Action_ReadDefender` | 54 | 67 | 14 | inferred_complete_timeline |
| `Action_PullBall` | 68 | 70 | 3 | inferred_complete_timeline |
| `Action_PullBall` | 73 | 77 | 5 | inferred_complete_timeline |
| `Action_None` | 78 | 82 | 5 | inferred_complete_timeline |
| `Action_ThrowPass` | 83 | 90 | 8 | inferred_complete_timeline |
| `Action_None` | 91 | 180 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 71 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 176 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_None` | 44 | 64 | 21 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_None` | 70 | 75 | 6 | inferred_complete_timeline |
| `Action_None` | 79 | 94 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 45 | 90 | 46 | inferred_complete_timeline |
| `Action_None` | 91 | 173 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 45 | 58 | 14 | inferred_complete_timeline |
| `Action_RunBlock` | 70 | 90 | 21 | inferred_complete_timeline |
| `Action_None` | 91 | 110 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 45 | 54 | 10 | inferred_complete_timeline |
| `Action_RunBlock` | 61 | 90 | 30 | inferred_complete_timeline |
| `Action_None` | 91 | 180 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 45 | 53 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 60 | 90 | 31 | inferred_complete_timeline |
| `Action_None` | 91 | 98 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 151 | 108 | inferred_complete_timeline |
| `Action_None` | 162 | 180 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 98 | 55 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 180 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 90 | 47 | inferred_complete_timeline |
| `Action_None` | 101 | 106 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 180 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 96 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 96 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 180 | 137 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 49–50 | 2 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 62–101 | 26 | 4 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 64–102 | 37 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 95–180 | 75 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 98–100 | 3 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 117–180 | 61 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 153–154 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 162–180 | 19 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 169–180 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `13` (2 segments found)
- ❌ Missing segment for action `Action_RunBlock` on target `16` (RG)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBall` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_RunBlock' for track '16' has invalid range: start=45, end=43. Clamping end to start.
- ⚠️ Action 'Action_None' range [44-176] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-151] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-180] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [45-53] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [56-57] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-98] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-98] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-96] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-173] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBall' range [68-70] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [45-58] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [70-90] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-110] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-71] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [45-54] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-96] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-64] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-75] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-94] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-72] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-98] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-116] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-160] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-180] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '25' has 1 frames without a visible bounding box.
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

</details>