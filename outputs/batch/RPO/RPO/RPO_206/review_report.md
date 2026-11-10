# Play-Annotation-Generator Annotation Review — RPO_206

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_206`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 21
- **Ball Tracks:** 0
- **Action Segments:** 64
- **Validation Warnings:** 44
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `19` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `2` | `2` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `3` | `3` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `11` | `11` | 46 | START | 46 | 48 |
| ✅ EXACT | `Action_RunBlock` | LG | `2` | `2` | 46 | START | 46 | 100 |
| ✅ EXACT | `Action_RunBlock` | RG | `3` | `3` | 46 | START | 46 | 100 |
| ✅ EXACT | `Action_RunBlock` | LT | `4` | `4` | 46 | START | 46 | 100 |
| ✅ EXACT | `Action_RunBlock` | RT | `7` | `7` | 46 | START | 46 | 100 |
| ✅ EXACT | `Action_ReadDefender` | QB | `12` | `12` | 49 | START | 49 | 71 |
| ✅ EXACT | `Action_PullBall` | QB | `12` | `12` | 72 | START | 72 | 81 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 94 | START | 94 | 100 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 49 | 71 | 23 | inferred_complete_timeline |
| `Action_PullBall` | 72 | 81 | 10 | inferred_complete_timeline |
| `Action_None` | 82 | 93 | 12 | inferred_complete_timeline |
| `Action_ThrowPass` | 94 | 100 | 7 | inferred_complete_timeline |
| `Action_None` | 101 | 110 | 10 | inferred_complete_timeline |
| `Action_None` | 120 | 150 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 110 | 66 | inferred_complete_timeline |
| `Action_None` | 115 | 120 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 150 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 45 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 46 | 100 | 55 | inferred_complete_timeline |
| `Action_None` | 101 | 150 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 45 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 46 | 100 | 55 | inferred_complete_timeline |
| `Action_None` | 101 | 150 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 45 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 46 | 48 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 51 | 100 | 50 | inferred_complete_timeline |
| `Action_None` | 101 | 144 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 45 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 46 | 100 | 55 | inferred_complete_timeline |
| `Action_None` | 101 | 150 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 45 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 46 | 100 | 55 | inferred_complete_timeline |
| `Action_None` | 101 | 150 | 50 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 150 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 67 | 23 | inferred_complete_timeline |
| `Action_None` | 74 | 79 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 150 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 52 | 8 | inferred_complete_timeline |
| `Action_None` | 85 | 89 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 108 | 64 | inferred_complete_timeline |
| `Action_None` | 110 | 150 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 100 | 56 | inferred_complete_timeline |
| `Action_None` | 102 | 116 | 15 | inferred_complete_timeline |
| `Action_None` | 123 | 150 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 146 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 150 | 106 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | Position_Unknown | Team_Unknown | 56–150 | 88 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 76–150 | 73 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 90–150 | 59 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 96–150 | 55 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 126–150 | 25 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 33 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [45-108] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-100] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-116] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-150] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-146] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-110] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [46-48] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-110] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-52] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-72] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-83] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-150] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-139] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-141] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-150] for track '20' has 2 frames without a visible bounding box.
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

</details>