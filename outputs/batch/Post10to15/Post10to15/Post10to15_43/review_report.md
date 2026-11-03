# Play-Annotation-Generator Annotation Review — Post10to15_43

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_43`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `11` | `11` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `21` | `21` |
| ✅ EXACT | `Action_RunPostRoute` | WR2 | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 13 | START | 13 | 17 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `11` | `11` | 16 | START | 16 | 34 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `15` | `15` | 16 | START | 18 | 72 |
| ✅ EXACT | `Action_PassBlock` | LT | `17` | `17` | 16 | START | 16 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 16 | START | 16 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 16 | START | 16 | 37 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `21` | `21` | 17 | END | 13 | 17 |
| ✅ EXACT | `Action_RunPostRoute` | WR2 | `1` | `1` | 25 | START | 25 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | Position_Unknown | `21` | `21` | 75 | START | 75 | 78 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 72 | 60 | inferred_complete_timeline |
| `Action_None` | 74 | 75 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 150 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 41 | 29 | inferred_complete_timeline |
| `Action_None` | 44 | 150 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_RunPostRoute` | 25 | 150 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 69 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 32 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 61 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 72 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 88 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 93 | 100 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_BallSnap` | 13 | 17 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 72 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 29 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 38 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 72 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 34 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 41 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 72 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 125 | 131 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 32 | 20 | inferred_complete_timeline |
| `Action_None` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_None` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_None` | 47 | 55 | 9 | inferred_complete_timeline |
| `Action_None` | 60 | 69 | 10 | inferred_complete_timeline |
| `Action_None` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_None` | 80 | 150 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 34 | 22 | inferred_complete_timeline |
| `Action_None` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_None` | 47 | 69 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 39 | 27 | inferred_complete_timeline |
| `Action_None` | 43 | 45 | 3 | inferred_complete_timeline |
| `Action_None` | 47 | 65 | 19 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 150 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 39 | 27 | inferred_complete_timeline |
| `Action_None` | 47 | 53 | 7 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 72 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 150 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 126 | 114 | inferred_complete_timeline |
| `Action_None` | 129 | 150 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 45 | 33 | inferred_complete_timeline |
| `Action_None` | 47 | 66 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 150 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 150 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 95 | 83 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–150 | 150 | 6 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–64 | 30 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 88–150 | 56 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 91–104 | 11 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 96–134 | 39 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 113–132 | 14 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 114–150 | 37 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 116–150 | 30 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 123–125 | 3 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 129–131 | 3 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 142–150 | 9 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 143–150 | 8 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 148–149 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (4 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `15` (C): Annotated start 16 != Inferred start 18
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ThrowPass` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 73 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [13–17], lower_priority='Action_PassBlock' annotated_start=16, effective_Action_PassBlock_start=18.
- ⚠️ Action 'Action_None' range [13-34] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-37] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-69] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [25-150] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-41] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-150] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-69] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-45] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-66] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-72] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-32] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-37] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-55] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-69] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-34] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [36-41] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-72] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [125-131] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-39] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-45] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-65] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-126] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-39] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-72] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-72] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-29] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [36-38] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-45] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-72] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-37] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-61] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-72] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-88] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [93-100] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [75-78] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [80-84] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-22] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-51] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-97] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-106] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-128] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-98] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-134] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-132] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-150] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '33' has 1 frames without a visible bounding box.
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

</details>