# Play-Annotation-Generator Annotation Review — InsideZoneRead_308

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_308`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 115
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `22` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | RG | offense | `12` | `11` |
| ✅ EXACT | `Action_ReadDefender` | RG | offense | `12` | `11` |
| ✅ EXACT | `Action_Keep` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 3 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `22` | `20` | 1 | START | 101 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `9` | 4 | START | 4 | 78 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `10` | 4 | START | 4 | 78 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `12` | `11` | 4 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 4 | START | 4 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `8` | 4 | START | 4 | 51 |
| ✅ EXACT | `Action_SnapReceive` | RG | `12` | `11` | 13 | END | 1 | 13 |
| ✅ EXACT | `Action_ReadDefender` | RG | `12` | `11` | 15 | START | 15 | 18 |
| ✅ EXACT | `Action_Keep` | RG | `12` | `11` | 19 | START | 19 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | `12` | `11` | 39 | START | 39 | 44 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 78 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 62 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 60 | 60 | inferred_complete_timeline |
| `Action_None` | 62 | 79 | 18 | inferred_complete_timeline |
| `Action_None` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_None` | 103 | 180 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 47 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 51 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 67 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 70 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 78 | 75 | inferred_complete_timeline |
| `Action_None` | 79 | 83 | 5 | inferred_complete_timeline |
| `Action_None` | 85 | 89 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 61 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 65 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 78 | 4 | inferred_complete_timeline |
| `Action_None` | 79 | 124 | 46 | inferred_complete_timeline |
| `Action_None` | 129 | 155 | 27 | inferred_complete_timeline |
| `Action_None` | 158 | 161 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 13 | 13 | inferred_complete_timeline |
| `Action_None` | 14 | 14 | 1 | inferred_complete_timeline |
| `Action_ReadDefender` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_Keep` | 19 | 38 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 39 | 44 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 49 | 55 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 76 | 89 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 92 | 103 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 78 | 75 | inferred_complete_timeline |
| `Action_None` | 79 | 180 | 102 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 62 | 62 | inferred_complete_timeline |
| `Action_None` | 72 | 180 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 103 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 92 | 92 | inferred_complete_timeline |
| `Action_None` | 103 | 156 | 54 | inferred_complete_timeline |
| `Action_None` | 159 | 180 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 106 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 109 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 6–58 | 34 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 44–56 | 13 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 62–180 | 119 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 77–144 | 59 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 84–125 | 42 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 101–180 | 77 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 110–127 | 18 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 119–148 | 30 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 123–158 | 31 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 126–144 | 19 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 132–180 | 39 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 136–154 | 19 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 140–144 | 5 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 141–180 | 21 | 5 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 145–180 | 36 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 145–180 | 36 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 145–180 | 36 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 149–153 | 5 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 154–180 | 27 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 159–180 | 22 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 166–175 | 10 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `22` (Position_Unknown): Annotated start 1 != Inferred start 101
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `12` (RG)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '11' has invalid range: start=4, end=0. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '20' has invalid range: start=101, end=13. Clamping end to start.
- ⚠️ Action 'Action_None' range [1-62] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-180] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-103] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-106] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-60] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-79] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-92] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-156] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-47] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-51] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-67] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-70] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-78] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-180] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [39-44] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [49-55] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [76-89] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [92-103] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-62] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-38] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-61] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-124] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-155] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-30] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-34] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-46] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-58] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-56] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-180] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-127] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-144] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-107] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-148] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-144] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-155] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-180] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-154] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-144] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-145] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-153] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-180] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-180] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-175] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '36' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_308'; source metadata written as null.

</details>