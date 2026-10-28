# Play-Annotation-Generator Annotation Review — Draw_5

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_5`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 64
- **Ball Tracks:** 0
- **Action Segments:** 127
- **Validation Warnings:** 198
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 1
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 3
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 110
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LT | offense | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `17` |
| ⚠️ START CHANGED | `Action_PassBlock` | RG | offense | `19` | `18` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | offense | `21` | `20` |
| ⚠️ START CHANGED | `Action_FakePassDroptoHandoff` | QB | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `21` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `18` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `19` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `20` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `21` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `9` | `Group` | 0 | START | 0 | 18 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 19 | START | 19 | 26 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LT | `14` | `13` | 26 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | `15` | `14` | 26 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `17` | `16` | 26 | START | 26 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `17` | 26 | START | 44 | 80 |
| ⚠️ START CHANGED | `Action_PassBlock` | RG | `19` | `18` | 26 | START | 44 | 80 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | `21` | `20` | 35 | END | N/A | N/A |
| ⚠️ START CHANGED | `Action_FakePassDroptoHandoff` | QB | `21` | `20` | 38 | START | 44 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `21` | `20` | 80 | START | 80 | 92 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 80 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 44–106
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_FakePassDroptoHandoff` | 44 | 79 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 80 | 92 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 103 | 106 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 44–106
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 44 | 106 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 26 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 26 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 26 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–18
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 18 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 44–106
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PassBlock` | 44 | 80 | 37 | inferred_complete_timeline |
| `Action_None` | 81 | 106 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_BallSnap` | 19 | 26 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 44–221
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PassBlock` | 44 | 80 | 37 | inferred_complete_timeline |
| `Action_None` | 81 | 106 | 26 | inferred_complete_timeline |
| `Action_None` | 150 | 221 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 26 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 26 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 26 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 26 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 26 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 26 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 26 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 26 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 26 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–5
- **Visible Samples:** 6

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 26 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–26 | 27 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 44–106 | 48 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 44–106 | 46 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 44–52 | 9 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 65–68 | 4 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 67–106 | 33 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 67–73 | 5 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 70–106 | 20 | 4 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 104–106 | 3 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 151–246 | 96 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 151–449 | 299 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 151–319 | 168 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 151–449 | 299 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 151–252 | 102 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 151–281 | 118 | 4 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 151–291 | 141 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 151–448 | 292 | 3 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 151–449 | 299 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 151–318 | 154 | 3 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 151–230 | 80 | 1 | Undefined position; Undefined team |
| `40` | `45` | Position_Unknown | Team_Unknown | 151–449 | 299 | 1 | Undefined position; Undefined team |
| `41` | `46` | Position_Unknown | Team_Unknown | 151–330 | 175 | 4 | Undefined position; Undefined team |
| `42` | `47` | Position_Unknown | Team_Unknown | 151–259 | 109 | 1 | Undefined position; Undefined team |
| `43` | `48` | Position_Unknown | Team_Unknown | 151–418 | 255 | 4 | Undefined position; Undefined team |
| `44` | `49` | Position_Unknown | Team_Unknown | 151–400 | 242 | 6 | Undefined position; Undefined team |
| `45` | `50` | Position_Unknown | Team_Unknown | 151–214 | 64 | 1 | Undefined position; Undefined team |
| `46` | `51` | Position_Unknown | Team_Unknown | 151–343 | 189 | 2 | Undefined position; Undefined team |
| `47` | `52` | Position_Unknown | Team_Unknown | 151–327 | 158 | 7 | Undefined position; Undefined team |
| `48` | `53` | Position_Unknown | Team_Unknown | 151–384 | 234 | 1 | Undefined position; Undefined team |
| `49` | `54` | Position_Unknown | Team_Unknown | 151–449 | 293 | 4 | Undefined position; Undefined team |
| `50` | `55` | Position_Unknown | Team_Unknown | 220–449 | 230 | 1 | Undefined position; Undefined team |
| `51` | `56` | Position_Unknown | Team_Unknown | 220–222 | 3 | 1 | Undefined position; Undefined team |
| `52` | `60` | Position_Unknown | Team_Unknown | 283–287 | 5 | 1 | Undefined position; Undefined team |
| `53` | `64` | Position_Unknown | Team_Unknown | 294–404 | 110 | 2 | Undefined position; Undefined team |
| `54` | `67` | Position_Unknown | Team_Unknown | 312–396 | 85 | 1 | Undefined position; Undefined team |
| `55` | `68` | Position_Unknown | Team_Unknown | 316–441 | 110 | 3 | Undefined position; Undefined team |
| `56` | `70` | Position_Unknown | Team_Unknown | 322–395 | 74 | 1 | Undefined position; Undefined team |
| `57` | `73` | Position_Unknown | Team_Unknown | 332–360 | 29 | 1 | Undefined position; Undefined team |
| `58` | `75` | Position_Unknown | Team_Unknown | 353–386 | 34 | 1 | Undefined position; Undefined team |
| `59` | `79` | Position_Unknown | Team_Unknown | 379–394 | 15 | 2 | Undefined position; Undefined team |
| `60` | `80` | Position_Unknown | Team_Unknown | 379–449 | 71 | 1 | Undefined position; Undefined team |
| `61` | `81` | Position_Unknown | Team_Unknown | 381–449 | 69 | 1 | Undefined position; Undefined team |
| `62` | `84` | Position_Unknown | Team_Unknown | 398–449 | 52 | 1 | Undefined position; Undefined team |
| `63` | `85` | Position_Unknown | Team_Unknown | 402–449 | 47 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_PassBlock` on target `14` (LT)
- ❌ Missing segment for action `Action_PassBlock` on target `15` (C)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `19` (RG): Annotated start 26 != Inferred start 44
- ❌ Missing segment for action `Action_SnapReceive` on target `21` (QB)
- ⚠️ `Action_FakePassDroptoHandoff` for actor_track_id `21` (QB): Annotated start 38 != Inferred start 44
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 44 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 44 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 88 |
| Missing visible bounding boxes during action | 105 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Segment 'Action_PassBlock' for track '13' has invalid range: start=26, end=18. Clamping end to start.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [19–26], lower_priority='Action_PassBlock' annotated_start=26, effective_Action_PassBlock_start=27.
- ⚠️ Segment 'Action_SnapReceive' for track '20' has invalid range: start=44, end=35. Clamping end to start.
- ⚠️ Action 'Action_None' range [19-26] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-26] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-26] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-26] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-26] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-26] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-26] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-26] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-26] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-26] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-26] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-26] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-18] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [19-26] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' for track '16' starts at frame 26, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PassBlock' range [26-26] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-106] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-221] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-106] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [80-92] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [103-106] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-62] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-68] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-106] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-48] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-106] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-52] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-68] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-80] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-106] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-69] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-76] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-98] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-246] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-449] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-222] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-319] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-449] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-252] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-185] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-263] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-281] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-291] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-413] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-426] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-448] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-449] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-184] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-304] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-318] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-230] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-187] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-206] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-221] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-330] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-259] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-193] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-389] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-404] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-418] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-222] for track '44' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-371] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-379] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-387] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-400] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-214] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-221] for track '46' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-343] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-188] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-221] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-267] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-322] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-384] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-383] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-424] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-440] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-449] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-312] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-404] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-396] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-356] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-422] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-441] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-395] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-360] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-386] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-386] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-394] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-404] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-449] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.

</details>