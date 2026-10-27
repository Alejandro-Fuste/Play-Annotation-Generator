# Play-Annotation-Generator Annotation Review — Counter_361

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_361`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 40
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 0
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 6
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 22
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `43` | `17` |
| ⚠️ START CHANGED | `Action_DownBlock` | Position_Unknown | Team_Unknown | `43` | `17` |
| ⚠️ START CHANGED | `Action_DownBlock` | Position_Unknown | Team_Unknown | `47` | `21` |
| ❌ MISSING SEGMENT | `Action_PullBlock` | RG | offense | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_PullLeadBlock` | TE2 | offense | `3` | `2` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_Handoff` | QB | offense | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 2 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 19 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `7` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 32 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `43` | `17` | 40 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_DownBlock` | Position_Unknown | `43` | `17` | 47 | START | 96 | 100 |
| ⚠️ START CHANGED | `Action_DownBlock` | Position_Unknown | `47` | `21` | 47 | START | 96 | 100 |
| ❌ MISSING SEGMENT | `Action_PullBlock` | RG | `14` | `13` | 47 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_PullLeadBlock` | TE2 | `3` | `2` | 47 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | `9` | `8` | 54 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_Handoff` | QB | `9` | `8` | 66 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `13` | `12` | 88 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 100 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 2–9
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 4 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 95 | 120 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 96 | 120 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–23
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 19–32
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 32 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–33
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 7 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 19 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 33 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

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
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 21–32
- **Visible Samples:** 12

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 32 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 20–33 | 14 | 1 | Undefined position; Undefined team |
| `16` | `42` | Position_Unknown | Team_Unknown | 96–120 | 25 | 1 | Undefined position; Undefined team |
| `17` | `43` | Position_Unknown | Team_Unknown | 96–120 | 25 | 2 | Undefined position; Undefined team |
| `18` | `44` | Position_Unknown | Team_Unknown | 96–120 | 25 | 1 | Undefined position; Undefined team |
| `19` | `45` | Position_Unknown | Team_Unknown | 96–120 | 25 | 1 | Undefined position; Undefined team |
| `20` | `46` | Position_Unknown | Team_Unknown | 96–120 | 25 | 1 | Undefined position; Undefined team |
| `21` | `47` | Position_Unknown | Team_Unknown | 96–120 | 25 | 2 | Undefined position; Undefined team |
| `22` | `48` | Position_Unknown | Team_Unknown | 96–120 | 25 | 1 | Undefined position; Undefined team |
| `23` | `49` | Position_Unknown | Team_Unknown | 96–120 | 25 | 1 | Undefined position; Undefined team |
| `24` | `50` | Position_Unknown | Team_Unknown | 96–120 | 25 | 1 | Undefined position; Undefined team |
| `25` | `51` | Position_Unknown | Team_Unknown | 96–120 | 25 | 1 | Undefined position; Undefined team |
| `26` | `53` | Position_Unknown | Team_Unknown | 96–120 | 25 | 1 | Undefined position; Undefined team |
| `27` | `54` | Position_Unknown | Team_Unknown | 96–120 | 25 | 1 | Undefined position; Undefined team |
| `28` | `55` | Position_Unknown | Team_Unknown | 96–120 | 25 | 1 | Undefined position; Undefined team |
| `29` | `56` | Position_Unknown | Team_Unknown | 96–120 | 25 | 1 | Undefined position; Undefined team |
| `30` | `57` | Position_Unknown | Team_Unknown | 96–120 | 25 | 1 | Undefined position; Undefined team |
| `31` | `58` | Position_Unknown | Team_Unknown | 96–120 | 25 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `17` (Position_Unknown)
- ⚠️ `Action_DownBlock` for actor_track_id `43` (Position_Unknown): Annotated start 47 != Inferred start 96
- ⚠️ `Action_DownBlock` for actor_track_id `47` (Position_Unknown): Annotated start 47 != Inferred start 96
- ❌ Missing segment for action `Action_PullBlock` on target `14` (RG)
- ❌ Missing segment for action `Action_PullLeadBlock` on target `3` (TE2)
- ❌ Missing segment for action `Action_SnapReceive` on target `9` (QB)
- ❌ Missing segment for action `Action_Handoff` on target `9` (QB)
- ❌ Missing segment for action `Action_BallCarry` on target `13` (RB)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 38 |
| Track-related warning | 11 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '20' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_PullLeadBlock' for track '2' has invalid range: start=47, end=32. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '8' has invalid range: start=40, end=32. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '8' has invalid range: start=66, end=32. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '12' has invalid range: start=88, end=9. Clamping end to start.
- ⚠️ Segment 'Action_PullBlock' for track '13' has invalid range: start=47, end=32. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '17' has invalid range: start=96, end=54. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-7] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-19] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-33] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-4] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-32] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-33] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-32] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-120] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-120] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-120] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-120] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-120] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-120] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-120] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-120] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-120] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-120] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>