# Play-Annotation-Generator Annotation Review — RPO_4

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_4`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `27` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `3` | `3` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `5` | `5` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `6` | `6` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBall` | QB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | RB | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `1` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `1` | `1` | 38 | START | 38 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `3` | `3` | 38 | START | 38 | 69 |
| ✅ EXACT | `Action_RunBlock` | RT | `4` | `4` | 38 | START | 38 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `5` | `5` | 38 | START | 38 | 43 |
| ✅ EXACT | `Action_RunBlock` | RG | `6` | `6` | 38 | START | 38 | 41 |
| ✅ EXACT | `Action_ReadDefender` | QB | `9` | `9` | 47 | START | 47 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBall` | QB | `9` | `9` | 57 | START | 57 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | RB | `7` | `7` | 76 | START | 78 | 79 |

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
- **Visible Frames:** 0–162
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 46 | 10 | inferred_complete_timeline |
| `Action_ReadDefender` | 47 | 56 | 10 | inferred_complete_timeline |
| `Action_PullBall` | 57 | 84 | 28 | inferred_complete_timeline |
| `Action_PullBall` | 88 | 131 | 44 | inferred_complete_timeline |
| `Action_PullBall` | 136 | 162 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 72 | 36 | inferred_complete_timeline |
| `Action_ThrowPass` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_ThrowPass` | 81 | 84 | 4 | inferred_complete_timeline |
| `Action_None` | 85 | 167 | 83 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 59 | 23 | inferred_complete_timeline |
| `Action_None` | 67 | 69 | 3 | inferred_complete_timeline |
| `Action_None` | 71 | 158 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 37 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 38 | 43 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 48 | 52 | 5 | inferred_complete_timeline |
| `Action_RunBlock` | 61 | 63 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 67 | 72 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 37 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 38 | 69 | 32 | inferred_complete_timeline |
| `Action_RunBlock` | 76 | 84 | 9 | inferred_complete_timeline |
| `Action_None` | 85 | 156 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 37 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 38 | 64 | 27 | inferred_complete_timeline |
| `Action_RunBlock` | 77 | 84 | 8 | inferred_complete_timeline |
| `Action_None` | 85 | 99 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–41
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 37 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 38 | 41 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 37 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 38 | 84 | 47 | inferred_complete_timeline |
| `Action_None` | 85 | 89 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 157 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 102 | 66 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 141 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 160 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 36 | 27 | inferred_complete_timeline |
| `Action_None` | 37 | 97 | 61 | inferred_complete_timeline |
| `Action_None` | 99 | 153 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 97 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 113 | 77 | inferred_complete_timeline |
| `Action_None` | 115 | 127 | 13 | inferred_complete_timeline |
| `Action_None` | 129 | 239 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 97 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 48 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | Position_Unknown | Team_Unknown | 50–141 | 92 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 74–93 | 20 | 1 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 79–89 | 9 | 2 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 85–88 | 4 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 94–221 | 118 | 2 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 95–159 | 64 | 2 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 95–102 | 8 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 103–239 | 137 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 103–239 | 137 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 112–140 | 10 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 120–171 | 50 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 124–191 | 63 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 138–164 | 27 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 138–225 | 83 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 142–187 | 45 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 144–198 | 51 | 2 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 220–236 | 6 | 2 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 231–239 | 8 | 2 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 234–235 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `5` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBall` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ThrowPass` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 64 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [37-97] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [38-64] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [77-84] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-99] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-157] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [38-69] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-156] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [38-43] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [48-52] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [61-63] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [67-72] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [38-41] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-72] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [78-79] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-113] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-127] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBall' range [57-84] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBall' range [88-131] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBall' range [136-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-97] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-102] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-141] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-160] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-48] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-158] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-97] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-153] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-141] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-83] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-88] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-209] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-151] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-159] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-117] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-147] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-140] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-155] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-191] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-164] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-225] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-165] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-187] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-191] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-237] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '34' has 1 frames without a visible bounding box.
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