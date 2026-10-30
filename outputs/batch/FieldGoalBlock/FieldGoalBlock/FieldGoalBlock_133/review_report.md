# Play-Annotation-Generator Annotation Review — FieldGoalBlock_133

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_133`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 419
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 140
- **Validation Warnings:** 167
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 125
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `8` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `8` | `8` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `4` | `4` |
| ✅ EXACT | `Action_BlockKick` | Right_Edge_Rusher | defense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `1` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `10` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `12` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `16` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `18` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `19` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `3` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `4` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `6` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `8` | `Group` | 0 | START | 0 | 35 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `8` | `8` | 36 | START | 36 | 48 |
| ✅ EXACT | `Action_KickBall` | Kicker | `4` | `4` | 61 | START | 61 | 64 |
| ✅ EXACT | `Action_BlockKick` | Right_Edge_Rusher | `5` | `5` | 64 | START | 64 | 82 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PlaceBall` | 36 | 48 | 13 | inferred_complete_timeline |
| `Action_None` | 49 | 213 | 165 | inferred_complete_timeline |
| `Action_None` | 219 | 220 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_KickBall` | 61 | 64 | 4 | inferred_complete_timeline |
| `Action_None` | 65 | 77 | 13 | inferred_complete_timeline |
| `Action_None` | 82 | 268 | 187 | inferred_complete_timeline |
| `Action_None` | 270 | 274 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 325 | 265 | inferred_complete_timeline |
| `Action_None` | 330 | 343 | 14 | inferred_complete_timeline |
| `Action_None` | 345 | 350 | 6 | inferred_complete_timeline |
| `Action_None` | 352 | 357 | 6 | inferred_complete_timeline |
| `Action_None` | 359 | 367 | 9 | inferred_complete_timeline |
| `Action_None` | 372 | 373 | 2 | inferred_complete_timeline |
| `Action_None` | 376 | 419 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 130 | 70 | inferred_complete_timeline |
| `Action_None` | 132 | 419 | 288 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–36
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 419 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 77 | 17 | inferred_complete_timeline |
| `Action_None` | 80 | 82 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 61 | 84 | 24 | inferred_complete_timeline |
| `Action_None` | 88 | 90 | 3 | inferred_complete_timeline |
| `Action_None` | 94 | 114 | 21 | inferred_complete_timeline |
| `Action_None` | 122 | 134 | 13 | inferred_complete_timeline |
| `Action_None` | 137 | 419 | 283 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–56
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 38 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 56 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 408 | 348 | inferred_complete_timeline |
| `Action_None` | 416 | 419 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 264 | 204 | inferred_complete_timeline |
| `Action_None` | 266 | 419 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_None` | 62 | 419 | 358 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–343
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 60 | 12 | inferred_complete_timeline |
| `Action_None` | 61 | 61 | 1 | inferred_complete_timeline |
| `Action_None` | 63 | 171 | 109 | inferred_complete_timeline |
| `Action_None` | 175 | 343 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–279
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 275 | 215 | inferred_complete_timeline |
| `Action_None` | 278 | 279 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–380
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 105 | 45 | inferred_complete_timeline |
| `Action_None` | 112 | 122 | 11 | inferred_complete_timeline |
| `Action_None` | 127 | 380 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 419 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 62 | 105 | 44 | inferred_complete_timeline |
| `Action_None` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 419 | 310 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 419 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–392
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 301 | 241 | inferred_complete_timeline |
| `Action_None` | 303 | 309 | 7 | inferred_complete_timeline |
| `Action_None` | 311 | 313 | 3 | inferred_complete_timeline |
| `Action_None` | 318 | 320 | 3 | inferred_complete_timeline |
| `Action_None` | 332 | 333 | 2 | inferred_complete_timeline |
| `Action_None` | 335 | 340 | 6 | inferred_complete_timeline |
| `Action_None` | 344 | 354 | 11 | inferred_complete_timeline |
| `Action_None` | 356 | 392 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_BlockKick` | 64 | 82 | 19 | inferred_complete_timeline |
| `Action_None` | 85 | 202 | 118 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_None` | 210 | 419 | 210 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 21–34 | 14 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 32–104 | 45 | 7 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 37–181 | 117 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 53–419 | 347 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 84–419 | 336 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 85–105 | 11 | 4 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 117–330 | 213 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 118–122 | 5 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 127–419 | 293 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 133–134 | 2 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 138–167 | 14 | 5 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 174–175 | 2 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 202–357 | 147 | 5 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 217–218 | 2 | 1 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 235–418 | 183 | 2 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 238–419 | 165 | 6 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 275–277 | 3 | 1 | Undefined position; Undefined team |
| `38` | `57` | Position_Unknown | Team_Unknown | 290–377 | 86 | 2 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 303–419 | 105 | 5 | Undefined position; Undefined team |
| `40` | `60` | Position_Unknown | Team_Unknown | 306–307 | 2 | 1 | Undefined position; Undefined team |
| `41` | `64` | Position_Unknown | Team_Unknown | 372–373 | 2 | 1 | Undefined position; Undefined team |
| `42` | `65` | Position_Unknown | Team_Unknown | 383–384 | 2 | 1 | Undefined position; Undefined team |
| `43` | `66` | Position_Unknown | Team_Unknown | 388–419 | 31 | 2 | Undefined position; Undefined team |
| `44` | `67` | Position_Unknown | Team_Unknown | 392–419 | 28 | 1 | Undefined position; Undefined team |
| `45` | `68` | Position_Unknown | Team_Unknown | 401–419 | 15 | 2 | Undefined position; Undefined team |
| `46` | `70` | Position_Unknown | Team_Unknown | 417–419 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Tackle` position mapped to `offense` team
- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 112 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_None' range [61-419] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-264] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-419] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-325] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-343] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-350] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-357] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-367] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-77] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-268] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-274] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [64-82] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-202] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-408] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-60] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '7' starts at frame 61, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [61-61] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-171] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-343] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-213] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-105] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-419] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-77] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-275] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-130] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-122] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-380] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-419] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-301] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-309] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-313] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-340] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-354] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-392] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-84] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-114] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-38] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-34] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-43] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-47] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-94] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-38] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-181] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-69] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-91] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-95] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-318] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-330] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-122] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-419] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-222] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-268] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-354] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-328] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-418] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-257] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-282] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-307] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-380] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-419] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-377] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-318] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-328] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-341] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-413] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-409] for track '45' has 1 frames without a visible bounding box.
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

</details>