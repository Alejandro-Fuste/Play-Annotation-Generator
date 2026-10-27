# Play-Annotation-Generator Annotation Review — Counter_74

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_74`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Fumble`
- **Result Frame:** 419
- **Player Tracks:** 51
- **Ball Tracks:** 0
- **Action Segments:** 121
- **Validation Warnings:** 191
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 0
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 7
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 107
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `16` | `14` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | RG | offense | `5` | `4` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | DT1 | defense | `6` | `5` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | RT | offense | `7` | `6` |
| ❌ MISSING SEGMENT | `Action_PullBlock` | LG | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_PullLeadBlock` | TE | offense | `11` | `10` |
| ⚠️ END CHANGED | `Action_SnapReceive` | SAF | defense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | LG | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 9 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 3 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `16` | `14` | 27 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_DownBlock` | RG | `5` | `4` | 35 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_DownBlock` | DT1 | `6` | `5` | 35 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_DownBlock` | RT | `7` | `6` | 35 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_PullBlock` | LG | `10` | `9` | 35 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_PullLeadBlock` | TE | `11` | `10` | 35 | START | N/A | N/A |
| ⚠️ END CHANGED | `Action_SnapReceive` | SAF | `12` | `11` | 41 | END | 27 | 29 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | LG | `10` | `9` | 66 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 66 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 9–24
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 24 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–19
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 19 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–29
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 26 | 22 | inferred_complete_timeline |
| `Action_None` | 27 | 29 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–29
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–29
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–29
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 29 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–29
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 29 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 14–29
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 26 | 13 | inferred_complete_timeline |
| `Action_None` | 27 | 29 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–29
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 29 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–29
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 29 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–29
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 26 | 3 | inferred_complete_timeline |
| `Action_None` | 27 | 29 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 5–29
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 26 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 29 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–29 | 30 | 2 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 15–19 | 5 | 1 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 21–29 | 9 | 2 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 69–361 | 278 | 5 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 69–328 | 258 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 69–335 | 262 | 4 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 69–248 | 170 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 69–287 | 219 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 69–286 | 218 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 69–281 | 213 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 69–264 | 188 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 69–215 | 140 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 69–387 | 314 | 5 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 69–340 | 230 | 5 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 69–197 | 129 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 69–419 | 311 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 69–245 | 167 | 5 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 69–413 | 285 | 6 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 69–419 | 324 | 5 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 231–419 | 165 | 10 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 236–238 | 3 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 239–419 | 136 | 4 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 243–419 | 121 | 3 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 257–330 | 69 | 2 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 267–277 | 11 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 275–419 | 145 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 284–419 | 136 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 288–419 | 132 | 1 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 300–391 | 81 | 2 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 314–419 | 106 | 1 | Undefined position; Undefined team |
| `43` | `53` | Position_Unknown | Team_Unknown | 326–419 | 77 | 3 | Undefined position; Undefined team |
| `44` | `54` | Position_Unknown | Team_Unknown | 335–340 | 6 | 1 | Undefined position; Undefined team |
| `45` | `55` | Position_Unknown | Team_Unknown | 336–419 | 77 | 2 | Undefined position; Undefined team |
| `46` | `56` | Position_Unknown | Team_Unknown | 339–375 | 37 | 1 | Undefined position; Undefined team |
| `47` | `59` | Position_Unknown | Team_Unknown | 380–419 | 23 | 4 | Undefined position; Undefined team |
| `48` | `60` | Position_Unknown | Team_Unknown | 383–419 | 37 | 1 | Undefined position; Undefined team |
| `49` | `61` | Position_Unknown | Team_Unknown | 388–390 | 3 | 1 | Undefined position; Undefined team |
| `50` | `62` | Position_Unknown | Team_Unknown | 399–416 | 16 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `14` (Position_Unknown)
- ❌ Missing segment for action `Action_DownBlock` on target `5` (RG)
- ❌ Missing segment for action `Action_DownBlock` on target `6` (DT1)
- ❌ Missing segment for action `Action_DownBlock` on target `7` (RT)
- ❌ Missing segment for action `Action_PullBlock` on target `10` (LG)
- ❌ Missing segment for action `Action_PullLeadBlock` on target `11` (TE)
- ❌ Missing segment for action `Action_BallCarry` on target `10` (LG)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 38 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 38 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 76 |
| Missing visible bounding boxes during action | 104 |
| Track-related warning | 10 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 150: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Track ID '14' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Segment 'Action_DownBlock' for track '4' has invalid range: start=35, end=29. Clamping end to start.
- ⚠️ Segment 'Action_DownBlock' for track '5' has invalid range: start=35, end=26. Clamping end to start.
- ⚠️ Segment 'Action_DownBlock' for track '6' has invalid range: start=35, end=29. Clamping end to start.
- ⚠️ Segment 'Action_PullBlock' for track '9' has invalid range: start=35, end=29. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '9' has invalid range: start=66, end=29. Clamping end to start.
- ⚠️ Segment 'Action_PullLeadBlock' for track '10' has invalid range: start=35, end=19. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '14' has invalid range: start=27, end=19. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-29] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-29] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-29] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-29] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-29] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-29] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-29] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-19] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [27-29] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-24] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-29] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-19] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-29] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-228] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-249] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-287] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-348] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-361] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-321] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-328] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-252] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-276] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-321] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-335] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-205] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-248] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-287] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-286] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-281] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-194] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-264] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-194] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-215] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-270] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-278] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-326] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-387] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-193] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-240] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-248] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-340] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-197] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-208] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-221] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-419] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-193] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-201] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-239] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-183] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-225] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-236] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-290] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-405] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-413] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-194] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-241] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-419] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-242] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-286] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-297] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-304] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-334] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-342] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-351] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-392] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-306] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-347] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-367] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-410] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-264] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-330] for track '36' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-277] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-419] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-419] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-321] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-391] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-382] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-340] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-346] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-375] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-383] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-405] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-413] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-390] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-410] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-416] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>