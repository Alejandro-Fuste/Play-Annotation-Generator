# Play-Annotation-Generator Annotation Review — InsideZoneRead_270

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_270`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 136
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 9
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | LT | offense | `13` | `12` |
| ✅ EXACT | `Action_ReadDefender` | LT | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `32` | `23` |
| ✅ EXACT | `Action_Keep` | LT | offense | `13` | `12` |
| ✅ EXACT | `Action_BallCarry` | LT | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `15` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `16` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_BallSnap` | QB | `19` | `18` | 3 | START | 3 | 14 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `14` | `13` | 6 | START | 6 | 84 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `14` | `13` | 6 | START | 6 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `16` | 6 | START | 6 | 84 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `18` | `17` | 6 | START | 6 | 80 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `8` | 6 | START | 6 | 84 |
| ✅ EXACT | `Action_SnapReceive` | LT | `13` | `12` | 14 | END | 3 | 14 |
| ✅ EXACT | `Action_ReadDefender` | LT | `13` | `12` | 21 | START | 21 | 30 |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | Position_Unknown | `32` | `23` | 30 | START | 140 | 140 |
| ✅ EXACT | `Action_Keep` | LT | `13` | `12` | 31 | START | 31 | 42 |
| ✅ EXACT | `Action_BallCarry` | LT | `13` | `12` | 43 | START | 43 | 135 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 84 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 3 | 14 | 12 | inferred_complete_timeline |
| `Action_None` | 15 | 140 | 126 | inferred_complete_timeline |
| `Action_None` | 144 | 210 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 73 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 77 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 73 | 71 | inferred_complete_timeline |
| `Action_None` | 76 | 171 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 14 | 12 | inferred_complete_timeline |
| `Action_None` | 15 | 20 | 6 | inferred_complete_timeline |
| `Action_ReadDefender` | 21 | 30 | 10 | inferred_complete_timeline |
| `Action_Keep` | 31 | 42 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 43 | 135 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 84 | 79 | inferred_complete_timeline |
| `Action_None` | 85 | 98 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 84 | 79 | inferred_complete_timeline |
| `Action_None` | 85 | 89 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 84 | 79 | inferred_complete_timeline |
| `Action_None` | 85 | 94 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 80 | 75 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 210 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 75 | 73 | inferred_complete_timeline |
| `Action_None` | 82 | 123 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 95 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 74 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 88 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 76 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 164 | 162 | inferred_complete_timeline |
| `Action_None` | 166 | 185 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 47 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 210 | 208 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–127 | 128 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 6–78 | 65 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 21–44 | 7 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 81–86 | 4 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 91–94 | 4 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 140–164 | 19 | 4 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 143–144 | 2 | 1 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 150–154 | 5 | 1 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 158–210 | 24 | 2 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 158–210 | 25 | 6 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 160–210 | 51 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 163–186 | 19 | 3 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 166–177 | 10 | 3 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 170–197 | 22 | 3 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 170–210 | 33 | 2 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 172–189 | 6 | 3 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 180–210 | 31 | 1 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 182–208 | 20 | 2 | Undefined position; Undefined team |
| `36` | `55` | Position_Unknown | Team_Unknown | 185–188 | 4 | 1 | Undefined position; Undefined team |
| `37` | `56` | Position_Unknown | Team_Unknown | 188–189 | 2 | 1 | Undefined position; Undefined team |
| `38` | `57` | Position_Unknown | Team_Unknown | 189–210 | 22 | 1 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 193–207 | 6 | 3 | Undefined position; Undefined team |
| `40` | `60` | Position_Unknown | Team_Unknown | 198–210 | 11 | 2 | Undefined position; Undefined team |
| `41` | `62` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |
| `42` | `63` | Position_Unknown | Team_Unknown | 207–208 | 2 | 1 | Undefined position; Undefined team |
| `43` | `64` | Position_Unknown | Team_Unknown | 207–208 | 2 | 1 | Undefined position; Undefined team |
| `44` | `65` | Position_Unknown | Team_Unknown | 208–210 | 3 | 1 | Undefined position; Undefined team |
| `45` | `66` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ `Action_BlockSecondLevel` for actor_track_id `32` (Position_Unknown): Annotated start 30 != Inferred start 140

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 75 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 540: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '12' has invalid range: start=6, end=2. Clamping end to start.
- ⚠️ Segment 'Action_BlockSecondLevel' for track '23' has invalid range: start=140, end=84. Clamping end to start.
- ⚠️ Action 'Action_None' range [3-127] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-76] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-88] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-47] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-73] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-75] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-123] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-94] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-164] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-185] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-74] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [43-135] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-98] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-171] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-80] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-140] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-8] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-70] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-22] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-44] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-154] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-154] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-172] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-183] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-210] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-168] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-186] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-177] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-189] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-197] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-189] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-208] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_270'; source metadata written as null.

</details>