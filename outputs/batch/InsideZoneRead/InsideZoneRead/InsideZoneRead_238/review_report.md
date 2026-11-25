# Play-Annotation-Generator Annotation Review — InsideZoneRead_238

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_238`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 71
- **Validation Warnings:** 88
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
- **Missing Segments:** 3
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DE2 | defense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `21` | `19` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `21` | `19` |
| ❌ MISSING SEGMENT | `Action_Keep` | Position_Unknown | Team_Unknown | `21` | `19` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 9 |
| ✅ EXACT | `Action_BallSnap` | DE2 | `5` | `4` | 7 | START | 7 | 20 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `1` | `0` | 10 | START | 10 | 70 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `11` | `10` | 10 | START | 10 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `13` | `12` | 10 | START | 10 | 40 |
| ✅ EXACT | `Action_ZoneBlock` | C | `15` | `14` | 10 | START | 10 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `8` | 10 | START | 10 | 63 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `21` | `19` | 20 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `21` | `19` | 25 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_Keep` | Position_Unknown | `21` | `19` | 33 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `21` | `19` | 47 | START | 78 | 109 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 70 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 97 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 109 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 62 | 56 | inferred_complete_timeline |
| `Action_None` | 97 | 108 | 12 | inferred_complete_timeline |
| `Action_None` | 111 | 146 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 60 | 54 | inferred_complete_timeline |
| `Action_None` | 64 | 107 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 10 | 70 | 61 | inferred_complete_timeline |
| `Action_None` | 71 | 109 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 10 | 70 | 61 | inferred_complete_timeline |
| `Action_None` | 71 | 148 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 10 | 31 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 10 | 63 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 70 | 5 | inferred_complete_timeline |
| `Action_None` | 71 | 102 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 10 | 40 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 45 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 67 | 17 | inferred_complete_timeline |
| `Action_None` | 74 | 108 | 35 | inferred_complete_timeline |
| `Action_None` | 112 | 130 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 110 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_BallSnap` | 7 | 20 | 14 | inferred_complete_timeline |
| `Action_None` | 21 | 87 | 67 | inferred_complete_timeline |
| `Action_None` | 98 | 123 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 73 | 67 | inferred_complete_timeline |
| `Action_None` | 75 | 115 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 115 | 109 | inferred_complete_timeline |
| `Action_None` | 128 | 180 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 109 | 103 | inferred_complete_timeline |
| `Action_None` | 111 | 180 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–15
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 15 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 40–108 | 69 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 44–76 | 19 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 50–180 | 131 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 65–180 | 106 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 78–109 | 32 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 100–104 | 5 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 109–134 | 10 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 110–130 | 21 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 111–180 | 62 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 111–150 | 40 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 112–114 | 3 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 113–178 | 60 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 133–137 | 5 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 136–180 | 45 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 157–177 | 19 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `19` (Position_Unknown)
- ❌ Missing segment for action `Action_ReadDefender` on target `19` (Position_Unknown)
- ❌ Missing segment for action `Action_Keep` on target `19` (Position_Unknown)
- ⚠️ `Action_BallCarry` for actor_track_id `21` (Position_Unknown): Annotated start 47 != Inferred start 78

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_SnapReceive' for track '19' has invalid range: start=78, end=20. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '19' has invalid range: start=78, end=32. Clamping end to start.
- ⚠️ Segment 'Action_Keep' for track '19' has invalid range: start=78, end=46. Clamping end to start.
- ⚠️ Action 'Action_None' range [71-148] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-109] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-60] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-107] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-15] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-87] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-123] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-110] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-97] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-109] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [10-63] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-102] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-62] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-108] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-146] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [10-70] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-109] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-115] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-180] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [10-40] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [42-45] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-67] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-108] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-130] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-73] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-115] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [10-31] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-51] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-76] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-180] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-145] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [78-109] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-104] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-114] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-130] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-121] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-166] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-150] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-161] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-178] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-137] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-169] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '29' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_238'; source metadata written as null.

</details>