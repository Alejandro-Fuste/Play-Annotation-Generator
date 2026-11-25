# Play-Annotation-Generator Annotation Review — InsideZoneRead_272

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_272`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `31` | `22` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `8` | `7` |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `17` | `16` |
| ❌ MISSING SEGMENT | `Action_Keep` | Position_Unknown | Team_Unknown | `17` | `16` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 7 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `31` | `22` | 8 | START | 84 | 84 |
| ✅ EXACT | `Action_ZoneBlock` | C | `10` | `9` | 11 | START | 11 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `16` | `15` | 11 | START | 11 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `3` | 11 | START | 11 | 35 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `8` | `7` | 11 | START | 11 | 77 |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | `17` | `16` | 23 | END | 24 | 24 |
| ✅ EXACT | `Action_ReadDefender` | Position_Unknown | `17` | `16` | 27 | START | 27 | 33 |
| ❌ MISSING SEGMENT | `Action_Keep` | Position_Unknown | `17` | `16` | 34 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `17` | `16` | 54 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 77 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 52 | 45 | inferred_complete_timeline |
| `Action_None` | 56 | 89 | 34 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 35 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 37 | 77 | 41 | inferred_complete_timeline |
| `Action_None` | 78 | 96 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 77 | 67 | inferred_complete_timeline |
| `Action_None` | 78 | 101 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 77 | 67 | inferred_complete_timeline |
| `Action_None` | 78 | 104 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 33 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 46 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 65 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 74 | 67 | inferred_complete_timeline |
| `Action_None` | 78 | 106 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 197 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 32 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 66 | 59 | inferred_complete_timeline |
| `Action_None` | 72 | 79 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 68 | 61 | inferred_complete_timeline |
| `Action_None` | 71 | 100 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–8 | 9 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 24–33 | 10 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 31–210 | 179 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 32–112 | 70 | 5 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 68–93 | 25 | 2 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 79–97 | 4 | 2 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 80–200 | 121 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 84–210 | 127 | 2 | Undefined position; Undefined team |
| `23` | `35` | Position_Unknown | Team_Unknown | 113–116 | 4 | 1 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 120–141 | 22 | 1 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 120–180 | 34 | 5 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 136–210 | 75 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 142–148 | 6 | 2 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 152–210 | 59 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 152–168 | 17 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 157–161 | 5 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 194–210 | 17 | 1 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 199–201 | 3 | 1 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 200–201 | 2 | 1 | Undefined position; Undefined team |
| `34` | `52` | Position_Unknown | Team_Unknown | 202–205 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `31` (Position_Unknown): Annotated start 8 != Inferred start 84
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ❌ Missing segment for action `Action_Keep` on target `17` (Position_Unknown)
- ❌ Missing segment for action `Action_BallCarry` on target `17` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 5 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 544: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_SnapReceive' for track '16' has invalid range: start=24, end=23. Clamping end to start.
- ⚠️ Segment 'Action_Keep' for track '16' has invalid range: start=34, end=33. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '16' has invalid range: start=54, end=33. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '22' has invalid range: start=84, end=23. Clamping end to start.
- ⚠️ Action 'Action_None' range [8-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-68] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-100] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-66] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-79] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-35] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-96] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-101] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-52] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-89] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-104] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-74] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-106] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-197] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-32] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 8, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [8-8] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-33] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [36-46] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [27-33] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-70] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-40] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-63] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-74] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-112] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-81] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-93] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-200] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-141] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-129] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-153] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-174] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-168] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-161] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '34' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_272'; source metadata written as null.

</details>