# Play-Annotation-Generator Annotation Review — RPO_17

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_17`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `10` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `8` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `10` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `11` | 40 | START | 40 | 44 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `13` | 40 | START | 40 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `14` | `14` | 40 | START | 40 | 47 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `5` | 40 | START | 40 | 98 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `8` | 40 | START | 40 | 45 |
| ✅ EXACT | `Action_ReadDefender` | QB | `4` | `4` | 46 | START | 46 | 51 |
| ✅ EXACT | `Action_PullBall` | QB | `4` | `4` | 52 | START | 52 | 64 |
| ✅ EXACT | `Action_ThrowPass` | QB | `4` | `4` | 80 | START | 80 | 98 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–283
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 45 | 7 | inferred_complete_timeline |
| `Action_ReadDefender` | 46 | 51 | 6 | inferred_complete_timeline |
| `Action_PullBall` | 52 | 64 | 13 | inferred_complete_timeline |
| `Action_None` | 65 | 79 | 15 | inferred_complete_timeline |
| `Action_ThrowPass` | 80 | 98 | 19 | inferred_complete_timeline |
| `Action_None` | 99 | 283 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 93 | 55 | inferred_complete_timeline |
| `Action_None` | 95 | 182 | 88 | inferred_complete_timeline |
| `Action_None` | 184 | 297 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 215 | 177 | inferred_complete_timeline |
| `Action_None` | 217 | 279 | 63 | inferred_complete_timeline |
| `Action_None` | 289 | 299 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 39 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 47 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 72 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 39 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 98 | 59 | inferred_complete_timeline |
| `Action_None` | 99 | 299 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 39 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 44 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 98 | 46 | inferred_complete_timeline |
| `Action_None` | 99 | 116 | 18 | inferred_complete_timeline |
| `Action_None` | 118 | 299 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–45
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 39 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 45 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 39 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 98 | 59 | inferred_complete_timeline |
| `Action_None` | 99 | 285 | 187 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 167 | 129 | inferred_complete_timeline |
| `Action_None` | 170 | 299 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 38 | 11 | inferred_complete_timeline |
| `Action_None` | 39 | 102 | 64 | inferred_complete_timeline |
| `Action_None` | 104 | 106 | 3 | inferred_complete_timeline |
| `Action_None` | 113 | 115 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 109 | 71 | inferred_complete_timeline |
| `Action_None` | 112 | 299 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 163 | 125 | inferred_complete_timeline |
| `Action_None` | 165 | 299 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 144 | 106 | inferred_complete_timeline |
| `Action_None` | 149 | 186 | 38 | inferred_complete_timeline |
| `Action_None` | 188 | 206 | 19 | inferred_complete_timeline |
| `Action_None` | 210 | 236 | 27 | inferred_complete_timeline |
| `Action_None` | 249 | 263 | 15 | inferred_complete_timeline |
| `Action_None` | 267 | 274 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–62
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 62 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 299 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 57 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 68–299 | 212 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 104–299 | 196 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 107–290 | 184 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 127–299 | 154 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 135–214 | 80 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 160–277 | 112 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 169–208 | 37 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 171–270 | 98 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 172–177 | 6 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 185–186 | 2 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 197–198 | 2 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 218–299 | 82 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 221–248 | 27 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 230–265 | 33 | 3 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 232–299 | 68 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 286–294 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 58 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [39-62] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-144] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-186] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-206] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-236] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-263] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-274] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-163] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-283] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-299] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-57] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-93] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-182] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-297] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-45] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-109] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-215] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-279] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-44] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-285] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-47] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [53-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '15' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-85] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-95] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-128] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-290] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-153] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-214] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-273] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-202] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-255] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-267] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-248] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-258] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-294] for track '31' has 2 frames without a visible bounding box.
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

</details>