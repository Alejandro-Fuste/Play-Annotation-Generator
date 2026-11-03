# Play-Annotation-Generator Annotation Review — SlantAndGo_27

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_27`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 163
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_SellRoute` | CB4 | defense | `2` | `2` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | CB4 | defense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 4 | START | 4 | 16 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | `13` | `13` | 7 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `5` | 19 | END | 4 | 19 |
| ✅ EXACT | `Action_SellRoute` | CB4 | `2` | `2` | 46 | START | 46 | 72 |
| ✅ EXACT | `Action_ThrowPass` | QB | `5` | `5` | 70 | START | 70 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | CB4 | `2` | `2` | 73 | START | 73 | 74 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 4 | 19 | 16 | inferred_complete_timeline |
| `Action_None` | 20 | 69 | 50 | inferred_complete_timeline |
| `Action_ThrowPass` | 70 | 77 | 8 | inferred_complete_timeline |
| `Action_None` | 78 | 87 | 10 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 124 | 8 | inferred_complete_timeline |
| `Action_None` | 126 | 130 | 5 | inferred_complete_timeline |
| `Action_None` | 133 | 138 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 102 | 99 | inferred_complete_timeline |
| `Action_None` | 126 | 210 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 80 | 77 | inferred_complete_timeline |
| `Action_None` | 82 | 87 | 6 | inferred_complete_timeline |
| `Action_None` | 89 | 148 | 60 | inferred_complete_timeline |
| `Action_None` | 154 | 210 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 198 | 195 | inferred_complete_timeline |
| `Action_None` | 204 | 207 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 13 | 10 | inferred_complete_timeline |
| `Action_None` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_None` | 19 | 20 | 2 | inferred_complete_timeline |
| `Action_None` | 22 | 26 | 5 | inferred_complete_timeline |
| `Action_None` | 30 | 31 | 2 | inferred_complete_timeline |
| `Action_None` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_None` | 38 | 46 | 9 | inferred_complete_timeline |
| `Action_None` | 88 | 210 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–16
- **Visible Samples:** 17

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 4 | 16 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–16
- **Visible Samples:** 17

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 16 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 210 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–4
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 4 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 210 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_SellRoute` | 46 | 72 | 27 | inferred_complete_timeline |
| `Action_VerticalStem` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_VerticalStem` | 76 | 210 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 210 | 207 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–95 | 94 | 4 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 29–30 | 2 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 32–44 | 6 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 83–99 | 16 | 2 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 84–210 | 125 | 2 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 91–157 | 35 | 5 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 91–121 | 12 | 4 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 93–134 | 41 | 2 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 96–129 | 13 | 3 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 98–210 | 112 | 2 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 102–175 | 29 | 4 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 105–107 | 3 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 105–173 | 51 | 4 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 126–127 | 2 | 1 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 133–210 | 78 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 136–141 | 5 | 2 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 155–156 | 2 | 1 | Undefined position; Undefined team |
| `32` | `54` | Position_Unknown | Team_Unknown | 173–178 | 6 | 1 | Undefined position; Undefined team |
| `33` | `55` | Position_Unknown | Team_Unknown | 173–178 | 6 | 1 | Undefined position; Undefined team |
| `34` | `56` | Position_Unknown | Team_Unknown | 184–210 | 18 | 3 | Undefined position; Undefined team |
| `35` | `57` | Position_Unknown | Team_Unknown | 185–205 | 18 | 2 | Undefined position; Undefined team |
| `36` | `59` | Position_Unknown | Team_Unknown | 188–210 | 23 | 1 | Undefined position; Undefined team |
| `37` | `60` | Position_Unknown | Team_Unknown | 189–210 | 22 | 1 | Undefined position; Undefined team |
| `38` | `63` | Position_Unknown | Team_Unknown | 193–210 | 18 | 1 | Undefined position; Undefined team |
| `39` | `68` | Position_Unknown | Team_Unknown | 197–210 | 13 | 2 | Undefined position; Undefined team |
| `40` | `69` | Position_Unknown | Team_Unknown | 198–210 | 13 | 1 | Undefined position; Undefined team |
| `41` | `71` | Position_Unknown | Team_Unknown | 202–207 | 5 | 2 | Undefined position; Undefined team |
| `42` | `73` | Position_Unknown | Team_Unknown | 204–210 | 7 | 1 | Undefined position; Undefined team |
| `43` | `76` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_PassBlock` on target `13` (C)
- ⚠️ Ambiguous match for action `Action_VerticalStem` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 32 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 32 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 64 |
| Missing visible bounding boxes during action | 92 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 40: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 40: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 40: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ Row 40: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [4–16], lower_priority='Action_PassBlock' annotated_start=7, effective_Action_PassBlock_start=17.
- ⚠️ Action 'Action_None' range [4-49] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-57] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-95] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-198] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SellRoute' range [46-72] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [73-74] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [76-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [70-77] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-87] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-124] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-80] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-148] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-102] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-16] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [4-16] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-13] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-17] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-20] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-26] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-31] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-36] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-46] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 4, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [4-4] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-30] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-35] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-90] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-99] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-86] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-113] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-100] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-134] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-104] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-107] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-175] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-142] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-173] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-178] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-178] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-198] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-199] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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