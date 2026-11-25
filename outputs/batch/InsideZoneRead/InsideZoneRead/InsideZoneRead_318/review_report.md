# Play-Annotation-Generator Annotation Review — InsideZoneRead_318

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_318`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 104
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 6
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 51
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `21` | `18` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `2` | `1` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `5` | `4` |
| ⚠️ END CHANGED | `Action_SnapReceive` | RT | offense | `15` | `14` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | RT | offense | `15` | `14` |
| ❌ MISSING SEGMENT | `Action_Keep` | RT | offense | `15` | `14` |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `16` | `15` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RT | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 47 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `21` | `18` | 73 | START | 78 | 87 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `15` | `14` | 76 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RG | `2` | `1` | 76 | START | 76 | 77 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `3` | `2` | 76 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `5` | `4` | 76 | START | 76 | 89 |
| ⚠️ END CHANGED | `Action_SnapReceive` | RT | `15` | `14` | 87 | END | 73 | 76 |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | RT | `15` | `14` | 95 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_Keep` | RT | `15` | `14` | 102 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | Position_Unknown | `16` | `15` | 107 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RT | `15` | `14` | 122 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 149 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 72 | 61 | inferred_complete_timeline |
| `Action_None` | 73 | 147 | 75 | inferred_complete_timeline |
| `Action_None` | 158 | 210 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 72 | 23 | inferred_complete_timeline |
| `Action_None` | 73 | 116 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 101 | 29 | inferred_complete_timeline |
| `Action_None` | 104 | 141 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 64 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 67 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 75 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 89 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 149 | 58 | inferred_complete_timeline |
| `Action_None` | 150 | 191 | 42 | inferred_complete_timeline |
| `Action_None` | 196 | 210 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 75 | 61 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 77 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_SnapReceive` | 73 | 76 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 37 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 59 | 16 | inferred_complete_timeline |
| `Action_None` | 76 | 106 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 72 | 12 | inferred_complete_timeline |
| `Action_None` | 73 | 166 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 72 | 43 | inferred_complete_timeline |
| `Action_None` | 73 | 210 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–34
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 72 | 1 | inferred_complete_timeline |
| `Action_None` | 73 | 73 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 93 | 21 | inferred_complete_timeline |
| `Action_None` | 95 | 116 | 22 | inferred_complete_timeline |
| `Action_None` | 119 | 210 | 92 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 7–26 | 20 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 8–44 | 37 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 26–99 | 56 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 29–210 | 161 | 4 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 41–67 | 14 | 3 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 66–87 | 20 | 3 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 70–85 | 10 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 80–210 | 128 | 3 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 99–172 | 74 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 108–119 | 12 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 116–200 | 85 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 118–163 | 46 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 124–180 | 48 | 4 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 175–181 | 7 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 198–210 | 10 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 208–210 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `21` (Position_Unknown): Annotated start 73 != Inferred start 78
- ❌ Missing segment for action `Action_ZoneBlock` on target `15` (RT)
- ❌ Missing segment for action `Action_ZoneBlock` on target `3` (LT)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ❌ Missing segment for action `Action_ReadDefender` on target `15` (RT)
- ❌ Missing segment for action `Action_Keep` on target `15` (RT)
- ❌ Missing segment for action `Action_BlockSecondLevel` on target `16` (Position_Unknown)
- ❌ Missing segment for action `Action_BallCarry` on target `15` (RT)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 6 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '2' has invalid range: start=76, end=64. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '14' has invalid range: start=76, end=72. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '14' has invalid range: start=95, end=76. Clamping end to start.
- ⚠️ Segment 'Action_Keep' for track '14' has invalid range: start=102, end=76. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '14' has invalid range: start=122, end=76. Clamping end to start.
- ⚠️ Segment 'Action_BlockSecondLevel' for track '15' has invalid range: start=107, end=26. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-166] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-77] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-64] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-67] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-89] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-191] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '5' starts at frame 73, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [73-73] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-116] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-93] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-116] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-101] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-141] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-147] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-37] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-59] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-106] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [73-76] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-26] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-44] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-33] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-99] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-62] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-190] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-55] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-67] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-67] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-87] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-85] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-125] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-172] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-119] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-200] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-163] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-148] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-161] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-181] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-202] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '30' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_318'; source metadata written as null.

</details>