# Play-Annotation-Generator Annotation Review — FieldGoalBlock_33

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_33`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 389
- **Player Tracks:** 55
- **Ball Tracks:** 0
- **Action Segments:** 164
- **Validation Warnings:** 212
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 149
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `9` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `11` | `11` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `2` | `2` |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher5 | defense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `1` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `11` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `13` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `14` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `17` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `18` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `2` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `7` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `9` | `Group` | 0 | START | 0 | 48 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `11` | `11` | 25 | START | 25 | 32 |
| ✅ EXACT | `Action_KickBall` | Kicker | `2` | `2` | 49 | START | 49 | 56 |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher5 | `10` | `10` | 62 | START | 62 | 68 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–360
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PlaceBall` | 25 | 32 | 8 | inferred_complete_timeline |
| `Action_None` | 33 | 354 | 322 | inferred_complete_timeline |
| `Action_None` | 359 | 360 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_KickBall` | 49 | 56 | 8 | inferred_complete_timeline |
| `Action_None` | 57 | 389 | 333 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 48 | 6 | inferred_complete_timeline |
| `Action_None` | 49 | 61 | 13 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_None` | 67 | 80 | 14 | inferred_complete_timeline |
| `Action_None` | 83 | 389 | 307 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_None` | 49 | 53 | 5 | inferred_complete_timeline |
| `Action_None` | 55 | 61 | 7 | inferred_complete_timeline |
| `Action_None` | 64 | 389 | 326 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 389 | 289 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 105 | 57 | inferred_complete_timeline |
| `Action_None` | 109 | 389 | 281 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 94 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_None` | 73 | 121 | 49 | inferred_complete_timeline |
| `Action_None` | 131 | 389 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 48 | 7 | inferred_complete_timeline |
| `Action_None` | 49 | 389 | 341 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 98 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–366
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_None` | 52 | 58 | 7 | inferred_complete_timeline |
| `Action_None` | 68 | 72 | 5 | inferred_complete_timeline |
| `Action_None` | 74 | 150 | 77 | inferred_complete_timeline |
| `Action_None` | 152 | 361 | 210 | inferred_complete_timeline |
| `Action_None` | 365 | 366 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–29
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 48 | 11 | inferred_complete_timeline |
| `Action_None` | 49 | 52 | 4 | inferred_complete_timeline |
| `Action_None` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_None` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_None` | 67 | 179 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 61 | 27 | inferred_complete_timeline |
| `Action_BlockKick` | 62 | 68 | 7 | inferred_complete_timeline |
| `Action_None` | 73 | 174 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 54 | 6 | inferred_complete_timeline |
| `Action_None` | 58 | 66 | 9 | inferred_complete_timeline |
| `Action_None` | 68 | 76 | 9 | inferred_complete_timeline |
| `Action_None` | 79 | 160 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–385
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 355 | 307 | inferred_complete_timeline |
| `Action_None` | 361 | 385 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–361
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 361 | 313 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–178 | 178 | 3 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–163 | 164 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 3–180 | 67 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 19–188 | 170 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 74–186 | 95 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 84–88 | 5 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 103–389 | 287 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 110–179 | 70 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 119–389 | 210 | 5 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 122–220 | 60 | 8 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 124–389 | 250 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 128–239 | 34 | 6 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 150–244 | 78 | 6 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 155–200 | 44 | 2 | Undefined position; Undefined team |
| `31` | `49` | Position_Unknown | Team_Unknown | 202–389 | 176 | 2 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 206–389 | 184 | 1 | Undefined position; Undefined team |
| `33` | `56` | Position_Unknown | Team_Unknown | 210–389 | 176 | 4 | Undefined position; Undefined team |
| `34` | `59` | Position_Unknown | Team_Unknown | 213–387 | 143 | 4 | Undefined position; Undefined team |
| `35` | `60` | Position_Unknown | Team_Unknown | 213–389 | 177 | 1 | Undefined position; Undefined team |
| `36` | `61` | Position_Unknown | Team_Unknown | 215–389 | 175 | 1 | Undefined position; Undefined team |
| `37` | `62` | Position_Unknown | Team_Unknown | 217–264 | 41 | 2 | Undefined position; Undefined team |
| `38` | `63` | Position_Unknown | Team_Unknown | 245–389 | 145 | 1 | Undefined position; Undefined team |
| `39` | `64` | Position_Unknown | Team_Unknown | 247–369 | 123 | 1 | Undefined position; Undefined team |
| `40` | `68` | Position_Unknown | Team_Unknown | 258–389 | 123 | 4 | Undefined position; Undefined team |
| `41` | `69` | Position_Unknown | Team_Unknown | 263–389 | 95 | 8 | Undefined position; Undefined team |
| `42` | `70` | Position_Unknown | Team_Unknown | 263–268 | 6 | 1 | Undefined position; Undefined team |
| `43` | `73` | Position_Unknown | Team_Unknown | 272–275 | 4 | 1 | Undefined position; Undefined team |
| `44` | `75` | Position_Unknown | Team_Unknown | 276–389 | 114 | 1 | Undefined position; Undefined team |
| `45` | `77` | Position_Unknown | Team_Unknown | 283–328 | 11 | 3 | Undefined position; Undefined team |
| `46` | `78` | Position_Unknown | Team_Unknown | 284–322 | 31 | 3 | Undefined position; Undefined team |
| `47` | `80` | Position_Unknown | Team_Unknown | 300–313 | 5 | 2 | Undefined position; Undefined team |
| `48` | `82` | Position_Unknown | Team_Unknown | 334–389 | 41 | 6 | Undefined position; Undefined team |
| `49` | `84` | Position_Unknown | Team_Unknown | 350–389 | 34 | 3 | Undefined position; Undefined team |
| `50` | `87` | Position_Unknown | Team_Unknown | 359–361 | 3 | 1 | Undefined position; Undefined team |
| `51` | `90` | Position_Unknown | Team_Unknown | 363–368 | 5 | 2 | Undefined position; Undefined team |
| `52` | `91` | Position_Unknown | Team_Unknown | 364–389 | 26 | 1 | Undefined position; Undefined team |
| `53` | `92` | Position_Unknown | Team_Unknown | 373–389 | 17 | 1 | Undefined position; Undefined team |
| `54` | `94` | Position_Unknown | Team_Unknown | 379–389 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Guard` position mapped to `offense` team
- ⚠️ 38 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 38 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_LongSnap' at frame 10 targets track ID '[?]', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 76 |
| Missing visible bounding boxes during action | 134 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 68: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_None' range [49-106] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-178] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-48] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-389] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-98] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-163] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-54] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-66] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-76] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-160] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-94] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-361] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-105] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-389] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-61] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [62-68] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-174] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-354] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-355] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-385] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-61] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-389] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-61] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-80] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-389] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-48] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-58] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-72] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-361] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-48] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-52] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-179] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-121] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-43] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-173] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-188] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-76] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-186] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-179] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-123] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-137] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-153] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-139] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-183] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-192] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-136] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-211] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-156] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-176] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-184] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-239] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-200] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-214] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-273] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-285] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-292] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-297] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-335] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-387] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-389] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-254] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-369] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-286] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-296] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-379] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-281] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-304] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-323] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-339] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-352] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-371] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-389] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-268] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-328] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-287] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-322] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-302] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-342] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-354] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-368] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-385] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-389] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-358] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-367] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-361] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-368] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-389] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.

</details>