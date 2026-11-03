# Play-Annotation-Generator Annotation Review — Post10to15_15

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_15`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 85
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `1` | `1` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB1 | offense | `5` | `5` |
| ✅ EXACT | `Action_RunPostRoute` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB1 | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 4 | START | 4 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 4 | START | 4 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 4 | START | 4 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `11` | `Group` | 4 | START | 4 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 4 | START | 4 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 4 | START | 4 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 4 | START | 4 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 4 | START | 4 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | `5` | `Group` | 4 | START | 4 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | `6` | `Group` | 4 | START | 4 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 4 | START | 4 | 24 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 25 | START | 25 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `1` | `1` | 31 | START | 31 | 62 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `12` | `12` | 31 | START | 38 | 180 |
| ✅ EXACT | `Action_PassBlock` | LG | `13` | `13` | 31 | START | 31 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `18` | `18` | 31 | START | 31 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 31 | START | 31 | 59 |
| ✅ EXACT | `Action_SnapReceive` | QB1 | `5` | `5` | 37 | END | 25 | 37 |
| ✅ EXACT | `Action_RunPostRoute` | WR1 | `0` | `0` | 50 | START | 50 | 137 |
| ✅ EXACT | `Action_ThrowPass` | QB1 | `5` | `5` | 94 | START | 94 | 100 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 4–173
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 24 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 25 | 37 | 13 | inferred_complete_timeline |
| `Action_None` | 38 | 93 | 56 | inferred_complete_timeline |
| `Action_ThrowPass` | 94 | 100 | 7 | inferred_complete_timeline |
| `Action_None` | 101 | 135 | 35 | inferred_complete_timeline |
| `Action_None` | 139 | 173 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>QB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 24 | 21 | inferred_complete_timeline |
| `Action_None` | 25 | 180 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 4–137
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 49 | 46 | inferred_complete_timeline |
| `Action_RunPostRoute` | 50 | 137 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 24 | 21 | inferred_complete_timeline |
| `Action_None` | 25 | 180 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 4–168
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 24 | 21 | inferred_complete_timeline |
| `Action_None` | 25 | 95 | 71 | inferred_complete_timeline |
| `Action_None` | 97 | 102 | 6 | inferred_complete_timeline |
| `Action_None` | 104 | 168 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 4–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 24 | 21 | inferred_complete_timeline |
| `Action_None` | 25 | 82 | 58 | inferred_complete_timeline |
| `Action_None` | 84 | 180 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 4–176
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 30 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 62 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 176 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 30 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 180 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 24 | 21 | inferred_complete_timeline |
| `Action_BallSnap` | 25 | 37 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 180 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 4–62
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 30 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 59 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 61 | 62 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 4–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 30 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 47 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 180 | 124 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 4–170
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 24 | 21 | inferred_complete_timeline |
| `Action_None` | 25 | 79 | 55 | inferred_complete_timeline |
| `Action_None` | 81 | 83 | 3 | inferred_complete_timeline |
| `Action_None` | 87 | 99 | 13 | inferred_complete_timeline |
| `Action_None` | 130 | 150 | 21 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 170 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 24 | 21 | inferred_complete_timeline |
| `Action_None` | 25 | 180 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 4–87
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 24 | 21 | inferred_complete_timeline |
| `Action_None` | 25 | 87 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 24 | 21 | inferred_complete_timeline |
| `Action_None` | 25 | 180 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 4–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 24 | 21 | inferred_complete_timeline |
| `Action_None` | 25 | 75 | 51 | inferred_complete_timeline |
| `Action_None` | 77 | 82 | 6 | inferred_complete_timeline |
| `Action_None` | 84 | 180 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 4–130
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 24 | 21 | inferred_complete_timeline |
| `Action_None` | 25 | 82 | 58 | inferred_complete_timeline |
| `Action_None` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_None` | 88 | 130 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 4–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 24 | 21 | inferred_complete_timeline |
| `Action_None` | 25 | 86 | 62 | inferred_complete_timeline |
| `Action_None` | 88 | 180 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 4–180
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 24 | 21 | inferred_complete_timeline |
| `Action_None` | 25 | 83 | 59 | inferred_complete_timeline |
| `Action_None` | 87 | 135 | 49 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 180 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 24 | 21 | inferred_complete_timeline |
| `Action_None` | 25 | 180 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 4–180
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 24 | 21 | inferred_complete_timeline |
| `Action_None` | 25 | 133 | 109 | inferred_complete_timeline |
| `Action_None` | 135 | 154 | 20 | inferred_complete_timeline |
| `Action_None` | 156 | 162 | 7 | inferred_complete_timeline |
| `Action_None` | 168 | 180 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 24 | 21 | inferred_complete_timeline |
| `Action_None` | 25 | 180 | 156 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 70–110 | 21 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 78–88 | 10 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 79–162 | 40 | 4 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 81–97 | 17 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 103–180 | 76 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 106–118 | 4 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 119–180 | 62 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 138–171 | 34 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 163–165 | 3 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `1` (2 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `12` (C): Annotated start 31 != Inferred start 38
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [25–37], lower_priority='Action_PassBlock' annotated_start=31, effective_Action_PassBlock_start=38.
- ⚠️ Action 'Action_RunPostRoute' range [50-137] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-62] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [65-176] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-82] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-130] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-180] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-87] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-173] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-86] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-95] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-82] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-180] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-180] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-79] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-99] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-170] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-154] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-47] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [57-180] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-59] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [61-62] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-75] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-180] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-76] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-110] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-88] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-81] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-115] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-152] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-162] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-97] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-180] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-171] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '31' has 1 frames without a visible bounding box.
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