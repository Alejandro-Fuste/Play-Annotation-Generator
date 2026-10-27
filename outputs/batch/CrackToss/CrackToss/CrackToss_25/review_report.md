# Play-Annotation-Generator Annotation Review — CrackToss_25

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_25`
- **Frame Range:** 0 to 298 (299 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 298
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_SnapReceive` | SAF | defense | `13` | `12` |
| ✅ EXACT | `Action_CrackBlock` | WR3 | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_PullBlock` | LT | offense | `19` | `18` |
| ⚠️ START CHANGED | `Action_PullBlock` | Position_Unknown | Team_Unknown | `24` | `22` |
| ✅ EXACT | `Action_Toss` | SAF | defense | `13` | `12` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `10` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 135 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 136 | START | 136 | 138 |
| ✅ EXACT | `Action_SnapReceive` | SAF | `13` | `12` | 138 | END | 136 | 138 |
| ✅ EXACT | `Action_CrackBlock` | WR3 | `10` | `9` | 139 | START | 139 | 204 |
| ⚠️ START CHANGED | `Action_PullBlock` | LT | `19` | `18` | 139 | START | 142 | 204 |
| ⚠️ START CHANGED | `Action_PullBlock` | Position_Unknown | `24` | `22` | 139 | START | 142 | 204 |
| ✅ EXACT | `Action_Toss` | SAF | `13` | `12` | 157 | START | 157 | 170 |
| ✅ EXACT | `Action_BallCarry` | RB | `4` | `3` | 171 | START | 171 | 291 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 204 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 3 | 4 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 8 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 14 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 28 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 33 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 48 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 56 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 89 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 107 | 12 | inferred_complete_timeline |
| `Action_None` | 140 | 158 | 19 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_BallCarry` | 171 | 291 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_None` | 136 | 222 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_None` | 136 | 298 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_CrackBlock` | 139 | 204 | 66 | inferred_complete_timeline |
| `Action_None` | 205 | 219 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 8 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 28 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 46 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 55 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 62 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 107 | 43 | inferred_complete_timeline |
| `Action_None` | 138 | 285 | 148 | inferred_complete_timeline |
| `Action_None` | 288 | 289 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 44 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 83 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 142 | 204 | 63 | inferred_complete_timeline |
| `Action_None` | 205 | 215 | 11 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_None` | 222 | 275 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_BallSnap` | 136 | 138 | 3 | inferred_complete_timeline |
| `Action_None` | 139 | 298 | 160 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_None` | 136 | 272 | 137 | inferred_complete_timeline |
| `Action_None` | 282 | 298 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 55 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–9
- **Visible Samples:** 10

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_None` | 136 | 298 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_None` | 136 | 298 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_None` | 136 | 222 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 115 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 135 | 18 | inferred_complete_timeline |
| `Action_SnapReceive` | 136 | 138 | 3 | inferred_complete_timeline |
| `Action_None` | 139 | 156 | 18 | inferred_complete_timeline |
| `Action_Toss` | 157 | 170 | 14 | inferred_complete_timeline |
| `Action_None` | 171 | 230 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–229 | 230 | 2 | Undefined position; Undefined team |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–298 | 297 | 3 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–298 | 290 | 4 | Undefined position; Undefined team |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–252 | 126 | 7 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 31–285 | 241 | 5 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 80–298 | 163 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 142–298 | 157 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 142–298 | 157 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 142–298 | 157 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 143–144 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 169–298 | 130 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 198–214 | 7 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 210–212 | 3 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 210–272 | 63 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 214–215 | 2 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 245–246 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 246–283 | 38 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 295–298 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PullBlock` for actor_track_id `19` (LT): Annotated start 139 != Inferred start 142
- ⚠️ `Action_PullBlock` for actor_track_id `24` (Position_Unknown): Annotated start 139 != Inferred start 142

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 52: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
- ⚠️ Action 'Action_None' range [136-272] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-222] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-229] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [171-291] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-276] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-220] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-238] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-298] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-219] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-165] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-201] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-228] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-252] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-222] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-115] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-230] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-55] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-4] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-8] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-14] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-28] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-33] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-48] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-56] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-89] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-158] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-8] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-28] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-46] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-55] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-62] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-107] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-285] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-44] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-83] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-215] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-275] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-48] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-111] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-129] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-285] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-214] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-272] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-283] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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

</details>