# Play-Annotation-Generator Annotation Review — Counter_284

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_284`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 156
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | TE | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 56 |
| ✅ EXACT | `Action_BallSnap` | TE | `4` | `3` | 57 | START | 57 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT | `11` | `10` | 60 | START | 60 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `16` | `15` | 60 | START | 71 | 86 |
| ✅ EXACT | `Action_PullBlock` | RG | `12` | `11` | 60 | START | 60 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `4` | `3` | 60 | START | 60 | 85 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 71 | END | 57 | 71 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `4` | 83 | START | 83 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `6` | 103 | START | 107 | 285 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 140 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_SnapReceive` | 57 | 71 | 15 | inferred_complete_timeline |
| `Action_None` | 72 | 82 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 83 | 102 | 20 | inferred_complete_timeline |
| `Action_None` | 103 | 299 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–295
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_BallCarry` | 107 | 285 | 179 | inferred_complete_timeline |
| `Action_BallCarry` | 294 | 295 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_BallSnap` | 57 | 59 | 3 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 60 | 85 | 26 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 91 | 114 | 24 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 111 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 56 | 3 | inferred_complete_timeline |
| `Action_None` | 57 | 72 | 16 | inferred_complete_timeline |
| `Action_None` | 81 | 94 | 14 | inferred_complete_timeline |
| `Action_None` | 98 | 111 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PullBlock` | 60 | 140 | 81 | inferred_complete_timeline |
| `Action_None` | 141 | 165 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 72 | 16 | inferred_complete_timeline |
| `Action_None` | 74 | 120 | 47 | inferred_complete_timeline |
| `Action_None` | 131 | 185 | 55 | inferred_complete_timeline |
| `Action_None` | 201 | 281 | 81 | inferred_complete_timeline |
| `Action_None` | 283 | 285 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 83 | 27 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 59 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 60 | 69 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 82 | 83 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 120 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 81 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 41–299
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 41 | 56 | 16 | inferred_complete_timeline |
| `Action_None` | 57 | 203 | 147 | inferred_complete_timeline |
| `Action_None` | 206 | 212 | 7 | inferred_complete_timeline |
| `Action_None` | 216 | 299 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–22 | 23 | 1 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–94 | 38 | 3 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 69–206 | 113 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 71–200 | 128 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 80–297 | 187 | 7 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 82–299 | 216 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 90–96 | 7 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 118–297 | 112 | 10 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 142–297 | 156 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 159–299 | 141 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 164–299 | 119 | 3 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 173–285 | 112 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 178–297 | 120 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 180–297 | 114 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 186–299 | 114 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 199–205 | 7 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 199–259 | 47 | 3 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 202–299 | 96 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 202–299 | 98 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 205–299 | 90 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 233–299 | 67 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 236–241 | 6 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 239–245 | 6 | 2 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 242–289 | 38 | 2 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 244–299 | 53 | 3 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 255–256 | 2 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 262–295 | 29 | 3 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |
| `43` | `53` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |
| `44` | `55` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |
| `45` | `56` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 34 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 34 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 68 |
| Missing visible bounding boxes during action | 87 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [57-81] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-111] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-72] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-94] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-111] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [60-85] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [91-114] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-83] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [107-285] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [294-295] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-72] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-185] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-281] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-120] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [60-69] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [82-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [60-140] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-165] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-72] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-94] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-203] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-212] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-299] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-118] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-206] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [71-86] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [88-105] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-200] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-144] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-167] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-213] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-297] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-124] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-297] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-122] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-172] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-212] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-227] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-237] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-297] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-297] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-294] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-271] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-285] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-297] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-186] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-193] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-209] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-297] for track '25' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-205] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-234] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-259] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-285] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-211] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-241] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-289] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-292] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-295] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>