# Play-Annotation-Generator Annotation Review — Counter_81

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_81`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `20` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 7 | START | 7 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 7 | START | 7 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 7 | START | 7 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 7 | START | 7 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 7 | START | 7 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 7 | START | 7 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 7 | START | 7 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 7 | START | 7 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 7 | START | 7 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 7 | START | 7 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `9` | `Group` | 7 | START | 7 | 54 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 51 | START | 51 | 67 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `12` | `11` | 51 | START | 51 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `13` | `12` | 55 | START | 55 | 78 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `15` | `14` | 55 | START | 68 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `22` | `21` | 55 | START | 55 | 101 |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | `9` | `8` | 55 | START | 55 | 131 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `20` | 67 | END | 51 | 67 |
| ✅ EXACT | `Action_Handoff` | QB | `21` | `20` | 75 | START | 75 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `12` | `11` | 89 | START | 89 | 117 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 131 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 7–238
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_SnapReceive` | 51 | 67 | 17 | inferred_complete_timeline |
| `Action_None` | 68 | 74 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 75 | 88 | 14 | inferred_complete_timeline |
| `Action_None` | 89 | 238 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 7–281
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 51 | 88 | 38 | inferred_complete_timeline |
| `Action_BallCarry` | 89 | 117 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 120 | 182 | 63 | inferred_complete_timeline |
| `Action_BallCarry` | 186 | 281 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 7–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_None` | 51 | 329 | 279 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 7–165
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_None` | 51 | 165 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 7–275
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_None` | 51 | 275 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 7–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 54 | 48 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 55 | 131 | 77 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 136 | 329 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 7–251
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_None` | 51 | 102 | 52 | inferred_complete_timeline |
| `Action_None` | 105 | 108 | 4 | inferred_complete_timeline |
| `Action_None` | 110 | 123 | 14 | inferred_complete_timeline |
| `Action_None` | 132 | 142 | 11 | inferred_complete_timeline |
| `Action_None` | 151 | 251 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 7–82
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 54 | 48 | inferred_complete_timeline |
| `Action_DownBlock` | 55 | 78 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 81 | 82 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 7–106
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_BallSnap` | 51 | 67 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 68 | 106 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 7–270
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 54 | 48 | inferred_complete_timeline |
| `Action_PullBlock` | 55 | 101 | 47 | inferred_complete_timeline |
| `Action_PullBlock` | 105 | 114 | 10 | inferred_complete_timeline |
| `Action_PullBlock` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 123 | 131 | 9 | inferred_complete_timeline |
| `Action_None` | 132 | 270 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 7–254
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_None` | 51 | 254 | 204 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 7–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_None` | 51 | 329 | 279 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 7–77
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_None` | 51 | 77 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 7–271
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_None` | 51 | 260 | 210 | inferred_complete_timeline |
| `Action_None` | 262 | 271 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 7–148
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_None` | 51 | 148 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 7–267
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_None` | 51 | 74 | 24 | inferred_complete_timeline |
| `Action_None` | 77 | 105 | 29 | inferred_complete_timeline |
| `Action_None` | 110 | 120 | 11 | inferred_complete_timeline |
| `Action_None` | 122 | 218 | 97 | inferred_complete_timeline |
| `Action_None` | 223 | 267 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 7–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_None` | 51 | 95 | 45 | inferred_complete_timeline |
| `Action_None` | 101 | 110 | 10 | inferred_complete_timeline |
| `Action_None` | 118 | 119 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 329 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 7–305
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_None` | 51 | 284 | 234 | inferred_complete_timeline |
| `Action_None` | 286 | 305 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 7–268
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_None` | 51 | 168 | 118 | inferred_complete_timeline |
| `Action_None` | 170 | 204 | 35 | inferred_complete_timeline |
| `Action_None` | 206 | 212 | 7 | inferred_complete_timeline |
| `Action_None` | 214 | 268 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 7–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_None` | 51 | 329 | 279 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 7–170
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_None` | 51 | 170 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 7–301
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_None` | 51 | 301 | 251 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 96–103 | 5 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 101–329 | 225 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 107–301 | 195 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 114–325 | 211 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 136–269 | 68 | 7 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 154–327 | 171 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 185–187 | 3 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 186–187 | 2 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 191–204 | 5 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 217–325 | 108 | 2 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 250–258 | 8 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 256–263 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `15` (C): Annotated start 55 != Inferred start 68
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [51–67], lower_priority='Action_DownBlock' annotated_start=55, effective_Action_DownBlock_start=68.
- ⚠️ Action 'Action_None' range [51-165] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-95] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-110] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-284] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-305] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-77] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-74] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-105] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-120] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-218] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-267] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-275] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [89-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [120-182] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [186-281] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [55-78] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [81-82] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-301] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [68-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-204] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-212] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-268] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-102] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-123] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-251] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-254] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-170] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-260] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-271] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-238] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [55-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [105-114] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [117-119] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-270] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-301] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-316] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-325] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-156] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-183] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-199] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-269] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-207] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-307] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-327] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-320] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-253] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-263] for track '33' has 2 frames without a visible bounding box.
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

</details>