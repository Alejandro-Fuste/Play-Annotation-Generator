# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_47

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_47`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 389
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 163
- **Validation Warnings:** 191
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 148
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `7` | `7` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_CatchKick` | Position_Unknown | Team_Unknown | `48` | `35` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `48` | `35` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `0` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `10` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `12` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `13` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `14` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `16` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `2` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `4` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `7` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `9` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `7` | `7` | 16 | START | 16 | 92 |
| ✅ EXACT | `Action_KickBall` | Kicker | `7` | `7` | 93 | START | 93 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_CatchKick` | Position_Unknown | `48` | `35` | 204 | START | 204 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `48` | `35` | 231 | START | 232 | 301 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_KickApproach` | 16 | 92 | 77 | inferred_complete_timeline |
| `Action_KickBall` | 93 | 97 | 5 | inferred_complete_timeline |
| `Action_None` | 98 | 186 | 89 | inferred_complete_timeline |
| `Action_None` | 192 | 194 | 3 | inferred_complete_timeline |
| `Action_None` | 199 | 201 | 3 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_None` | 215 | 389 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 343 | 328 | inferred_complete_timeline |
| `Action_None` | 348 | 389 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 389 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 389 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–384
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 384 | 369 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 389 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 153 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 149 | 134 | inferred_complete_timeline |
| `Action_None` | 152 | 171 | 20 | inferred_complete_timeline |
| `Action_None` | 174 | 220 | 47 | inferred_complete_timeline |
| `Action_None` | 222 | 300 | 79 | inferred_complete_timeline |
| `Action_None` | 304 | 389 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 389 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–349
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 266 | 251 | inferred_complete_timeline |
| `Action_None` | 270 | 339 | 70 | inferred_complete_timeline |
| `Action_None` | 348 | 349 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 389 | 374 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 98 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 124 | 109 | inferred_complete_timeline |
| `Action_None` | 135 | 140 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 132 | 117 | inferred_complete_timeline |
| `Action_None` | 136 | 260 | 125 | inferred_complete_timeline |
| `Action_None` | 268 | 320 | 53 | inferred_complete_timeline |
| `Action_None` | 323 | 389 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–375
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 200 | 185 | inferred_complete_timeline |
| `Action_None` | 204 | 209 | 6 | inferred_complete_timeline |
| `Action_None` | 211 | 375 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 208 | 193 | inferred_complete_timeline |
| `Action_None` | 210 | 246 | 37 | inferred_complete_timeline |
| `Action_None` | 251 | 389 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 270 | 255 | inferred_complete_timeline |
| `Action_None` | 273 | 298 | 26 | inferred_complete_timeline |
| `Action_None` | 306 | 389 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–364 | 321 | 13 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–174 | 154 | 11 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 25–185 | 83 | 16 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 53–54 | 2 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 77–91 | 9 | 3 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 94–115 | 12 | 3 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 97–389 | 292 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 97–166 | 56 | 6 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 115–389 | 272 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 121–385 | 263 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 128–389 | 257 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 133–140 | 8 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 136–157 | 12 | 4 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 144–311 | 163 | 3 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 150–166 | 14 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 153–389 | 234 | 2 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 155–206 | 29 | 4 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 186–188 | 3 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 187–389 | 193 | 8 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 196–275 | 61 | 7 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 196–202 | 7 | 1 | Undefined position; Undefined team |
| `38` | `60` | Position_Unknown | Team_Unknown | 233–234 | 2 | 1 | Undefined position; Undefined team |
| `39` | `61` | Position_Unknown | Team_Unknown | 240–262 | 23 | 1 | Undefined position; Undefined team |
| `40` | `63` | Position_Unknown | Team_Unknown | 247–251 | 4 | 2 | Undefined position; Undefined team |
| `41` | `67` | Position_Unknown | Team_Unknown | 256–262 | 6 | 2 | Undefined position; Undefined team |
| `42` | `74` | Position_Unknown | Team_Unknown | 319–389 | 71 | 1 | Undefined position; Undefined team |
| `43` | `75` | Position_Unknown | Team_Unknown | 327–329 | 3 | 1 | Undefined position; Undefined team |
| `44` | `76` | Position_Unknown | Team_Unknown | 337–375 | 39 | 1 | Undefined position; Undefined team |
| `45` | `82` | Position_Unknown | Team_Unknown | 366–389 | 18 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CatchKick` and target `48` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `48` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 49, Column 'Cross Goal Line': Unknown actor track ID '?' in entry '670,?'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 131 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_None' range [16-389] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-384] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-98] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-343] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-389] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-270] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-298] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-208] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-246] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-186] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-389] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-124] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-140] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-153] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-200] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-209] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-375] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-266] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-339] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-149] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-171] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-220] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-300] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-389] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-132] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-260] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-320] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-389] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-15] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-19] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-57] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-81] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-98] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-118] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-124] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-237] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-307] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-364] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-29] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-35] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-129] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-153] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-167] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-27] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-35] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-63] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-103] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-146] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-174] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-182] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-91] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-285] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-103] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-118] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-130] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-166] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-355] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-385] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-354] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-379] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-389] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-140] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-307] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-166] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-164] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-174] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-200] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchKick' range [204-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchKick' range [214-218] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-223] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [232-301] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-223] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-248] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-261] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-262] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-375] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-373] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-389] for track '45' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'KickoffReturnTouchdown_47'; source metadata written as null.

</details>