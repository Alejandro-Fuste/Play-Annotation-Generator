# Play-Annotation-Generator Annotation Review — FieldGoalBlock_132

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_132`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 449
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 176
- **Validation Warnings:** 231
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 9
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 165
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `8` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `2` | `2` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `0` | `0` |
| ✅ EXACT | `Action_BlockKick` | Position_Unknown | Team_Unknown | `20` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `0` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `2` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `3` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `5` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `7` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `8` | `Group` | 0 | START | 0 | 4 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `2` | `2` | 15 | START | 15 | 29 |
| ✅ EXACT | `Action_KickBall` | Kicker | `0` | `0` | 31 | START | 31 | 42 |
| ✅ EXACT | `Action_BlockKick` | Position_Unknown | `20` | `19` | 42 | START | 42 | 57 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–36
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PlaceBall` | 15 | 29 | 15 | inferred_complete_timeline |
| `Action_None` | 30 | 30 | 1 | inferred_complete_timeline |
| `Action_None` | 33 | 36 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_KickBall` | 31 | 42 | 12 | inferred_complete_timeline |
| `Action_None` | 45 | 47 | 3 | inferred_complete_timeline |
| `Action_None` | 53 | 55 | 3 | inferred_complete_timeline |
| `Action_None` | 57 | 63 | 7 | inferred_complete_timeline |
| `Action_None` | 92 | 144 | 53 | inferred_complete_timeline |
| `Action_None` | 149 | 178 | 30 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 185 | 190 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–315
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 100 | 70 | inferred_complete_timeline |
| `Action_None` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_None` | 111 | 212 | 102 | inferred_complete_timeline |
| `Action_None` | 215 | 250 | 36 | inferred_complete_timeline |
| `Action_None` | 260 | 265 | 6 | inferred_complete_timeline |
| `Action_None` | 270 | 273 | 4 | inferred_complete_timeline |
| `Action_None` | 280 | 286 | 7 | inferred_complete_timeline |
| `Action_None` | 291 | 306 | 16 | inferred_complete_timeline |
| `Action_None` | 310 | 315 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 57 | 87 | 31 | inferred_complete_timeline |
| `Action_None` | 99 | 101 | 3 | inferred_complete_timeline |
| `Action_None` | 103 | 164 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 8 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 30 | 1 | inferred_complete_timeline |
| `Action_None` | 31 | 157 | 127 | inferred_complete_timeline |
| `Action_None` | 159 | 161 | 3 | inferred_complete_timeline |
| `Action_None` | 163 | 165 | 3 | inferred_complete_timeline |
| `Action_None` | 170 | 173 | 4 | inferred_complete_timeline |
| `Action_None` | 176 | 191 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 58 | 59 | 2 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_None` | 71 | 89 | 19 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 147 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 105 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 23 | 11 | inferred_complete_timeline |
| `Action_None` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_None` | 45 | 47 | 3 | inferred_complete_timeline |
| `Action_None` | 55 | 60 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–416
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 81 | 51 | inferred_complete_timeline |
| `Action_None` | 92 | 101 | 10 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 113 | 7 | inferred_complete_timeline |
| `Action_None` | 116 | 131 | 16 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 180 | 42 | inferred_complete_timeline |
| `Action_None` | 183 | 246 | 64 | inferred_complete_timeline |
| `Action_None` | 250 | 282 | 33 | inferred_complete_timeline |
| `Action_None` | 289 | 389 | 101 | inferred_complete_timeline |
| `Action_None` | 399 | 416 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 30 | 5 | inferred_complete_timeline |
| `Action_None` | 31 | 53 | 23 | inferred_complete_timeline |
| `Action_None` | 89 | 163 | 75 | inferred_complete_timeline |
| `Action_None` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_None` | 170 | 173 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 3–443 | 389 | 12 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 9–449 | 439 | 3 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 12–239 | 217 | 8 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 12–168 | 94 | 8 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 21–75 | 55 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 24–25 | 2 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 25–105 | 72 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 32–81 | 50 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 34–209 | 171 | 8 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 42–157 | 113 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 75–187 | 72 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 77–173 | 91 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 86–148 | 62 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 88–180 | 93 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 93–195 | 95 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 101–139 | 5 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 106–337 | 159 | 3 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 121–182 | 62 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 125–223 | 82 | 3 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 143–208 | 62 | 3 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 201–423 | 203 | 5 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 201–438 | 232 | 2 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 222–328 | 95 | 3 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 244–449 | 205 | 2 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 269–449 | 174 | 3 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 284–314 | 28 | 4 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 303–444 | 139 | 3 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 304–449 | 141 | 2 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 311–436 | 117 | 6 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 322–449 | 119 | 5 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 349–449 | 101 | 1 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 359–449 | 90 | 2 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 396–399 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `FG_Block_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 163 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 266: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_KickBall' range [31-42] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-47] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-55] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-63] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-144] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-178] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-190] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-105] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '2' starts at frame 30, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [30-30] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-36] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-89] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-147] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-87] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-164] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-81] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-101] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-113] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-131] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-180] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-246] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-282] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-389] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-416] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-100] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-212] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-250] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-286] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-306] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-315] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-8] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-157] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-191] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-53] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-163] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-23] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-47] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-60] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-7] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-30] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-88] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-96] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-231] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-265] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-341] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-410] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-419] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-422] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-436] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-194] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-449] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-22] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-55] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-63] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-110] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-213] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-28] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-38] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-54] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-105] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-75] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-28] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-105] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-41] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [42-57] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-160] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-172] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-179] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-82] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-157] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-128] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-187] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-103] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-173] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-106] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-148] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-113] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-142] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-195] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-211] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-282] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-337] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-182] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-135] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-204] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-223] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-168] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-208] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-209] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-217] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-276] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-377] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-423] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-312] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-438] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-290] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-328] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-287] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-351] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-384] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-449] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-294] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-309] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-314] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-345] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-395] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-444] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-319] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-336] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-342] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-379] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-407] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-414] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-436] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-354] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-436] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-443] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-449] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-449] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-386] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-399] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>