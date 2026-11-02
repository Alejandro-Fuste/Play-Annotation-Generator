# Play-Annotation-Generator Annotation Review — WRSlowScreens_40

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `WRSlowScreens_40`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_WRSlowScreens`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 46
- **Ball Tracks:** 1
- **Action Segments:** 106
- **Validation Warnings:** 145
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `13` | `13` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `6` | `6` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_RunAfterCatch` | Position_Unknown | Team_Unknown | `30` | `28` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 3 | START | 3 | 19 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `11` | `11` | 6 | START | 20 | 55 |
| ✅ EXACT | `Action_PassBlock` | RG | `13` | `13` | 6 | START | 6 | 25 |
| ✅ EXACT | `Action_PassBlock` | LT | `5` | `5` | 6 | START | 6 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `6` | `6` | 6 | START | 6 | 119 |
| ✅ EXACT | `Action_PassBlock` | RT | `9` | `9` | 6 | START | 6 | 236 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 19 | END | 3 | 19 |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | `12` | `12` | 69 | START | 69 | 77 |
| ✅ EXACT | `Action_RunAfterCatch` | Position_Unknown | `30` | `28` | 124 | START | 124 | 146 |

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
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 19 | 17 | inferred_complete_timeline |
| `Action_None` | 20 | 68 | 49 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 69 | 77 | 9 | inferred_complete_timeline |
| `Action_None` | 78 | 102 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 50 | 48 | inferred_complete_timeline |
| `Action_None` | 52 | 57 | 6 | inferred_complete_timeline |
| `Action_None` | 59 | 72 | 14 | inferred_complete_timeline |
| `Action_None` | 74 | 124 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 10 | 8 | inferred_complete_timeline |
| `Action_None` | 14 | 151 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 239 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 119 | 114 | inferred_complete_timeline |
| `Action_PassBlock` | 124 | 126 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 128 | 130 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 132 | 239 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 3 | 19 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 55 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–25
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 25 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 236 | 231 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 205 | 203 | inferred_complete_timeline |
| `Action_None` | 222 | 223 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 81 | 79 | inferred_complete_timeline |
| `Action_None` | 83 | 236 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 38 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 239 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 136 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 205 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 117 | 115 | inferred_complete_timeline |
| `Action_None` | 119 | 172 | 54 | inferred_complete_timeline |
| `Action_None` | 174 | 239 | 66 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 13–104 | 64 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 27–233 | 170 | 5 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 33–239 | 191 | 4 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 53–227 | 163 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 78–80 | 3 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 88–98 | 11 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 95–96 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 98–122 | 25 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 98–239 | 122 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 99–208 | 110 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 100–239 | 116 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 117–239 | 89 | 7 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 117–146 | 30 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 117–120 | 4 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 126–132 | 7 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 131–198 | 63 | 2 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 131–132 | 2 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 140–239 | 99 | 2 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 150–239 | 89 | 2 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 158–236 | 63 | 5 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 161–193 | 33 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 169–239 | 68 | 2 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 187–236 | 50 | 1 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 233–239 | 7 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 237–238 | 2 | 1 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |
| `44` | `53` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |
| `45` | `54` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |
| `46` | `55` | Position_Unknown | Team_Unknown | 237–238 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | 17 | 23 | 6 | 85.7% | 18 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `11` (C): Annotated start 6 != Inferred start 20
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [3–19], lower_priority='Action_PassBlock' annotated_start=6, effective_Action_PassBlock_start=20.
- ⚠️ Action 'Action_None' range [3-205] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-38] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-205] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-81] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-236] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-239] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-119] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [124-126] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [128-130] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [132-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-117] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-172] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-236] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-50] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-57] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-72] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-124] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-55] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-68] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-102] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-25] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-10] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-151] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-18] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-60] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-104] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-52] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-177] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-217] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-225] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-233] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-36] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-80] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-236] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-58] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-223] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-98] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-122] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-178] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-236] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-208] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-163] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-218] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-179] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-228] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [124-146] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-132] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-181] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-198] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-146] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-239] for track '33' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-201] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-239] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-189] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-213] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-193] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-215] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-239] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-236] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

</details>