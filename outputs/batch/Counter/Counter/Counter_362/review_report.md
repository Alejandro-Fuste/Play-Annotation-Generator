# Play-Annotation-Generator Annotation Review — Counter_362

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_362`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 62
- **Validation Warnings:** 113
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 3
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 47
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `15` | `14` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `5` | `4` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `6` | `5` |
| ⚠️ START CHANGED | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `1` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `15` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 19 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 23 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `15` | `14` | 24 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | `15` | `14` | 30 | START | N/A | N/A |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `5` | `4` | 30 | START | 30 | 61 |
| ✅ EXACT | `Action_PullBlock` | RG | `6` | `5` | 30 | START | 30 | 61 |
| ⚠️ START CHANGED | `Action_PullLeadBlock` | Position_Unknown | `1` | `0` | 30 | START | 48 | 61 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 37 | END | 24 | 37 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `15` | 49 | START | 49 | 61 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | `16` | `15` | 71 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 82 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 19–61
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 23 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 24 | 37 | 14 | inferred_complete_timeline |
| `Action_None` | 38 | 48 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 49 | 61 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 61 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–2
- **Visible Samples:** 3

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 61 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–5
- **Visible Samples:** 6

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PullBlock` | 30 | 61 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 31 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–9
- **Visible Samples:** 10

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 61 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 24–45
- **Visible Samples:** 12

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_None` | 35 | 37 | 3 | inferred_complete_timeline |
| `Action_None` | 39 | 45 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 61 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 61 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 61 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 61 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 61 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–61 | 20 | 2 | Undefined position; Undefined team |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–61 | 62 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 36–61 | 26 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 47–61 | 15 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `31` | `32` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `32` | `33` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `33` | `34` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `34` | `35` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `35` | `36` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `36` | `37` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `37` | `38` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `38` | `39` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `39` | `40` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `40` | `41` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `41` | `42` | Position_Unknown | Team_Unknown | 190–203 | 14 | 1 | Undefined position; Undefined team |
| `42` | `43` | Position_Unknown | Team_Unknown | 193–209 | 13 | 2 | Undefined position; Undefined team |
| `43` | `44` | Position_Unknown | Team_Unknown | 200–210 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `15` (C)
- ❌ Missing segment for action `Action_DownBlock` on target `15` (C)
- ⚠️ `Action_PullLeadBlock` for actor_track_id `1` (Position_Unknown): Annotated start 30 != Inferred start 48
- ❌ Missing segment for action `Action_BallCarry` on target `16` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 725: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 726: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '14' has invalid range: start=24, end=5. Clamping end to start.
- ⚠️ Segment 'Action_DownBlock' for track '14' has invalid range: start=30, end=5. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '15' has invalid range: start=71, end=61. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [48-61] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-61] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-61] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-61] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [30-61] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [30-61] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-61] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-61] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-61] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-61] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-31] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-61] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [49-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-25] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-37] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-61] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-61] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-203] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-199] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-209] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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