# Play-Annotation-Generator Annotation Review — OutsideZoneRead_120

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_120`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 117
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_Keep` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `18` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `3` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_BallSnap` | C | `3` | `2` | 1 | START | 1 | 10 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `13` | `12` | 4 | START | 4 | 81 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `3` | `2` | 4 | START | 11 | 81 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `4` | 4 | START | 4 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `8` | `7` | 4 | START | 4 | 19 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `9` | `8` | 4 | START | 4 | 81 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 10 | END | 1 | 10 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `12` | `11` | 15 | START | 15 | 26 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `8` | `7` | 20 | START | 20 | 77 |
| ✅ EXACT | `Action_Keep` | QB | `12` | `11` | 27 | START | 27 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `12` | `11` | 47 | START | 47 | 112 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 81 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 10 | 10 | inferred_complete_timeline |
| `Action_None` | 11 | 14 | 4 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 15 | 26 | 12 | inferred_complete_timeline |
| `Action_Keep` | 27 | 46 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 47 | 112 | 66 | inferred_complete_timeline |
| `Action_BallCarry` | 116 | 164 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 77 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 122 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 81 | 78 | inferred_complete_timeline |
| `Action_None` | 82 | 210 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 81 | 78 | inferred_complete_timeline |
| `Action_None` | 82 | 210 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 10 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 81 | 71 | inferred_complete_timeline |
| `Action_None` | 82 | 87 | 6 | inferred_complete_timeline |
| `Action_None` | 91 | 94 | 4 | inferred_complete_timeline |
| `Action_None` | 97 | 133 | 37 | inferred_complete_timeline |
| `Action_None` | 136 | 166 | 31 | inferred_complete_timeline |
| `Action_None` | 168 | 192 | 25 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 201 | 205 | 5 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 81 | 78 | inferred_complete_timeline |
| `Action_None` | 82 | 126 | 45 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 137 | 191 | 55 | inferred_complete_timeline |
| `Action_None` | 202 | 205 | 4 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 19 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 20 | 77 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 171 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 127 | 127 | inferred_complete_timeline |
| `Action_None` | 132 | 135 | 4 | inferred_complete_timeline |
| `Action_None` | 145 | 195 | 51 | inferred_complete_timeline |
| `Action_None` | 203 | 210 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 21 | 21 | inferred_complete_timeline |
| `Action_None` | 25 | 77 | 53 | inferred_complete_timeline |
| `Action_None` | 84 | 210 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 15 | 15 | inferred_complete_timeline |
| `Action_None` | 17 | 81 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 126 | 126 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 156 | 16 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 104 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 73 | 73 | inferred_complete_timeline |
| `Action_None` | 77 | 91 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 70 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 103 | 103 | inferred_complete_timeline |
| `Action_None` | 117 | 168 | 52 | inferred_complete_timeline |
| `Action_None` | 181 | 210 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–97 | 96 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 29–210 | 115 | 5 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 75–197 | 106 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 78–210 | 133 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 78–79 | 2 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 118–210 | 88 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 126–210 | 85 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 132–210 | 70 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 135–210 | 76 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 142–210 | 63 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 146–190 | 43 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 152–210 | 43 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 170–185 | 16 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 176–203 | 19 | 4 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 191–210 | 20 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 195–210 | 13 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `3` (C): Annotated start 4 != Inferred start 11
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 242: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '2' (C): higher_priority='Action_BallSnap' [1–10], lower_priority='Action_ZoneBlock' annotated_start=4, effective_Action_ZoneBlock_start=11.
- ⚠️ Action 'Action_None' range [1-73] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-91] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-133] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-166] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-192] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-205] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-77] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-127] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-195] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-103] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-168] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [20-77] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-36] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-97] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-171] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [47-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [116-164] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-126] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-191] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-70] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-104] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-21] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-77] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-210] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-15] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-81] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-122] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-156] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-33] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-110] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-127] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-197] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-187] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-197] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-185] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-195] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-185] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-196] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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

</details>