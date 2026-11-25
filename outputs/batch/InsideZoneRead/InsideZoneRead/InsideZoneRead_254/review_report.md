# Play-Annotation-Generator Annotation Review — InsideZoneRead_254

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_254`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `8` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `26` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | LT | offense | `16` | `15` |
| ✅ EXACT | `Action_ReadDefender` | LT | offense | `16` | `15` |
| ✅ EXACT | `Action_Keep` | LT | offense | `16` | `15` |
| ✅ EXACT | `Action_BlockSecondLevel` | RB | offense | `4` | `3` |
| ✅ EXACT | `Action_BallCarry` | LT | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `6` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `8` | `Group` | 0 | START | 0 | 17 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `26` | `21` | 18 | START | 62 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `9` | 21 | START | 21 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `13` | 21 | START | 21 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `14` | 21 | START | 21 | 67 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `16` | `15` | 21 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RG | `7` | `6` | 21 | START | 21 | 113 |
| ✅ EXACT | `Action_SnapReceive` | LT | `16` | `15` | 33 | END | 18 | 33 |
| ✅ EXACT | `Action_ReadDefender` | LT | `16` | `15` | 39 | START | 39 | 48 |
| ✅ EXACT | `Action_Keep` | LT | `16` | `15` | 49 | START | 49 | 65 |
| ✅ EXACT | `Action_BlockSecondLevel` | RB | `4` | `3` | 55 | START | 55 | 113 |
| ✅ EXACT | `Action_BallCarry` | LT | `16` | `15` | 66 | START | 66 | 200 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 113 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 122 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 54 | 6 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 55 | 113 | 59 | inferred_complete_timeline |
| `Action_None` | 114 | 210 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 210 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 95 | 78 | inferred_complete_timeline |
| `Action_None` | 98 | 178 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_SnapReceive` | 18 | 33 | 16 | inferred_complete_timeline |
| `Action_None` | 34 | 38 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 39 | 48 | 10 | inferred_complete_timeline |
| `Action_Keep` | 49 | 65 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 66 | 200 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 79 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 67 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 113 | 35 | inferred_complete_timeline |
| `Action_None` | 114 | 210 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 113 | 93 | inferred_complete_timeline |
| `Action_None` | 114 | 210 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 63 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 69 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 78 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 93 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 113 | 19 | inferred_complete_timeline |
| `Action_None` | 114 | 156 | 43 | inferred_complete_timeline |
| `Action_None` | 164 | 168 | 5 | inferred_complete_timeline |
| `Action_None` | 171 | 210 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–37
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 22 | 5 | inferred_complete_timeline |
| `Action_None` | 24 | 27 | 4 | inferred_complete_timeline |
| `Action_None` | 30 | 37 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 106 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 48 | 31 | inferred_complete_timeline |
| `Action_None` | 52 | 210 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 43 | 26 | inferred_complete_timeline |
| `Action_None` | 52 | 80 | 29 | inferred_complete_timeline |
| `Action_None` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_None` | 97 | 210 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>LB4 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 195 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 128 | 111 | inferred_complete_timeline |
| `Action_None` | 131 | 210 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 161 | 144 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–69 | 70 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 17–26 | 10 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 21–113 | 93 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 30–210 | 181 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 53–199 | 147 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 62–191 | 127 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 83–210 | 128 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 134–156 | 23 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 137–139 | 3 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 158–210 | 53 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 174–186 | 13 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 176–207 | 32 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 181–210 | 25 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 187–210 | 24 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `26` (Position_Unknown): Annotated start 18 != Inferred start 62
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `16` (LT)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 7 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 508: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 508: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (RG) duration 93 frames exceeds threshold 90 frames [start=21, end=113].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (RT) duration 93 frames exceeds threshold 90 frames [start=21, end=113].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (C) duration 93 frames exceeds threshold 90 frames [start=21, end=113].
- ⚠️ Segment 'Action_ZoneBlock' for track '15' has invalid range: start=21, end=17. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '21' has invalid range: start=62, end=33. Clamping end to start.
- ⚠️ Action 'Action_None' range [18-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-106] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-48] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-122] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-95] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-178] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-210] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-43] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-80] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [21-63] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-69] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-78] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-93] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-113] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-210] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-195] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-69] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-161] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [21-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [21-67] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [18-33] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [49-65] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [66-200] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-22] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-27] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-37] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-26] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-113] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-199] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-67] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-191] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-156] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-186] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-207] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_254'; source metadata written as null.

</details>