# Play-Annotation-Generator Annotation Review — Counter_158

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_158`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 128
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_PlaySideFakeStep` | LT | offense | `13` | `12` |
| ✅ EXACT | `Action_BallSnap` | WR3 | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DE2 | defense | `16` | `15` |
| ✅ EXACT | `Action_DownBlock` | RB | offense | `17` | `16` |
| ✅ EXACT | `Action_DownBlock` | WR3 | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | WR4 | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | SAF2 | defense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | LB1 | defense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | LB1 | defense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | LT | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `19` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `20` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `21` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `22` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `3` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 0 | START | 0 | 83 |
| ✅ EXACT | `Action_PlaySideFakeStep` | LT | `13` | `12` | 82 | START | 82 | 138 |
| ✅ EXACT | `Action_BallSnap` | WR3 | `8` | `7` | 84 | START | 84 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DE2 | `16` | `15` | 87 | START | 87 | 186 |
| ✅ EXACT | `Action_DownBlock` | RB | `17` | `16` | 87 | START | 87 | 186 |
| ✅ EXACT | `Action_DownBlock` | WR3 | `8` | `7` | 87 | START | 87 | 116 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | WR4 | `3` | `2` | 87 | START | 87 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | SAF2 | `5` | `4` | 89 | START | 89 | 152 |
| ✅ EXACT | `Action_SnapReceive` | LB1 | `11` | `10` | 101 | END | 84 | 101 |
| ✅ EXACT | `Action_Handoff` | LB1 | `11` | `10` | 115 | START | 115 | 138 |
| ✅ EXACT | `Action_BallCarry` | LT | `13` | `12` | 139 | START | 139 | 155 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 186 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–259
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 177 | 94 | inferred_complete_timeline |
| `Action_None` | 179 | 203 | 25 | inferred_complete_timeline |
| `Action_None` | 210 | 259 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_DownBlock` | 87 | 186 | 100 | inferred_complete_timeline |
| `Action_None` | 187 | 264 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 359 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–282
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 282 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_BallSnap` | 84 | 86 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 87 | 116 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_PullBlock` | 87 | 123 | 37 | inferred_complete_timeline |
| `Action_PullBlock` | 126 | 186 | 61 | inferred_complete_timeline |
| `Action_None` | 187 | 268 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 82 | 138 | 57 | inferred_complete_timeline |
| `Action_BallCarry` | 139 | 155 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 148–252
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 148 | 162 | 15 | inferred_complete_timeline |
| `Action_None` | 166 | 252 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 127–128
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 135–309
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 135 | 272 | 138 | inferred_complete_timeline |
| `Action_None` | 274 | 279 | 6 | inferred_complete_timeline |
| `Action_None` | 282 | 309 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 145–147
- **Visible Samples:** 3

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 145 | 147 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 116 | 33 | inferred_complete_timeline |
| `Action_None` | 118 | 123 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_DownBlock` | 87 | 186 | 100 | inferred_complete_timeline |
| `Action_None` | 187 | 205 | 19 | inferred_complete_timeline |
| `Action_None` | 208 | 255 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 53 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 66 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 254 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–261
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_SnapReceive` | 84 | 101 | 18 | inferred_complete_timeline |
| `Action_None` | 102 | 114 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 115 | 138 | 24 | inferred_complete_timeline |
| `Action_None` | 139 | 261 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 223 | 140 | inferred_complete_timeline |
| `Action_None` | 225 | 230 | 6 | inferred_complete_timeline |
| `Action_None` | 241 | 253 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 162 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 120 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 123 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 265 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 89 | 152 | 64 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 161 | 169 | 9 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 171 | 176 | 6 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 180 | 186 | 7 | inferred_complete_timeline |
| `Action_None` | 187 | 280 | 94 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 167–342 | 176 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 172–241 | 69 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 181–359 | 174 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 186–341 | 139 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 188–262 | 74 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 189–216 | 11 | 3 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 190–242 | 53 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 233–236 | 4 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 238–296 | 59 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 241–259 | 19 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 249–259 | 9 | 2 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 289–314 | 26 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 291–322 | 11 | 4 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 299–310 | 12 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 301–306 | 4 | 2 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 303–334 | 28 | 3 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 310–318 | 9 | 1 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 312–333 | 10 | 2 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 312–329 | 14 | 3 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 317–326 | 10 | 1 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 325–327 | 3 | 1 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 325–333 | 8 | 2 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 353–359 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `5` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '2' (WR4) duration 100 frames exceeds threshold 90 frames [start=87, end=186].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '15' (DE2) duration 100 frames exceeds threshold 90 frames [start=87, end=186].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '16' (RB) duration 100 frames exceeds threshold 90 frames [start=87, end=186].
- ⚠️ Action 'Action_None' range [84-162] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [87-123] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-268] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-282] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [89-152] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [161-169] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [171-176] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-280] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-223] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-230] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-253] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-123] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [87-116] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-116] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-120] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [115-138] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-261] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-265] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [82-138] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [139-155] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-254] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-177] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-203] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-259] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [87-186] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-205] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-255] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-264] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-53] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-66] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-272] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-279] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-309] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-162] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-252] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-342] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-234] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-241] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-343] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-322] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-257] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-262] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-242] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-296] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-259] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-255] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-314] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-314] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-310] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-318] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-334] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-318] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-333] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-325] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-326] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-333] for track '43' has 2 frames without a visible bounding box.
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

</details>