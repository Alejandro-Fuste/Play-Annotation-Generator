# Play-Annotation-Generator Annotation Review — InsideZoneRead_293

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_293`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT2 | defense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | CB3 | defense | `12` | `11` |
| ✅ EXACT | `Action_ReadDefender` | CB3 | defense | `12` | `11` |
| ✅ EXACT | `Action_Keep` | CB3 | defense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | CB3 | defense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `10` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 24 |
| ✅ EXACT | `Action_BallSnap` | DT2 | `13` | `12` | 22 | START | 22 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `10` | 25 | START | 25 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `19` | 25 | START | 25 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 25 | START | 25 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `22` | `21` | 25 | START | 25 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `8` | `7` | 25 | START | 25 | 27 |
| ✅ EXACT | `Action_SnapReceive` | CB3 | `12` | `11` | 35 | END | 22 | 35 |
| ✅ EXACT | `Action_ReadDefender` | CB3 | `12` | `11` | 40 | START | 40 | 47 |
| ✅ EXACT | `Action_Keep` | CB3 | `12` | `11` | 48 | START | 48 | 68 |
| ✅ EXACT | `Action_BallCarry` | CB3 | `12` | `11` | 69 | START | 69 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 122 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 138 | 117 | inferred_complete_timeline |
| `Action_None` | 170 | 210 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 94 | 73 | inferred_complete_timeline |
| `Action_None` | 96 | 108 | 13 | inferred_complete_timeline |
| `Action_None` | 114 | 210 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 210 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 103 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 160 | 139 | inferred_complete_timeline |
| `Action_None` | 165 | 210 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 210 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 122 | 98 | inferred_complete_timeline |
| `Action_None` | 123 | 210 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 32 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_None` | 131 | 133 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 170 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–44
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 27 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 30 | 44 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 106 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 122 | 15 | inferred_complete_timeline |
| `Action_None` | 123 | 210 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 27 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 122 | 92 | inferred_complete_timeline |
| `Action_None` | 123 | 210 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 59 | 38 | inferred_complete_timeline |
| `Action_None` | 63 | 189 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 62 | 41 | inferred_complete_timeline |
| `Action_None` | 65 | 88 | 24 | inferred_complete_timeline |
| `Action_None` | 90 | 210 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–25
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 25 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_BallSnap` | 22 | 35 | 14 | inferred_complete_timeline |
| `Action_None` | 36 | 123 | 88 | inferred_complete_timeline |
| `Action_None` | 125 | 127 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 97 | 76 | inferred_complete_timeline |
| `Action_None` | 102 | 210 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 162 | 141 | inferred_complete_timeline |
| `Action_None` | 170 | 201 | 32 | inferred_complete_timeline |
| `Action_None` | 203 | 210 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 98 | 77 | inferred_complete_timeline |
| `Action_None` | 101 | 108 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 108 | 87 | inferred_complete_timeline |
| `Action_None` | 117 | 152 | 36 | inferred_complete_timeline |
| `Action_None` | 156 | 210 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 22 | 35 | 14 | inferred_complete_timeline |
| `Action_None` | 36 | 39 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 40 | 47 | 8 | inferred_complete_timeline |
| `Action_Keep` | 48 | 68 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 69 | 210 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 186 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 125 | 104 | inferred_complete_timeline |
| `Action_None` | 127 | 130 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 31–210 | 169 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 54–73 | 11 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 59–210 | 143 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 84–210 | 122 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 121–210 | 90 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 143–210 | 59 | 4 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 148–210 | 63 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 175–210 | 34 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 183–189 | 7 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 189–194 | 5 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 196–210 | 15 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 198–210 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 4 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 98 frames exceeds threshold 90 frames [start=25, end=122].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RG) duration 98 frames exceeds threshold 90 frames [start=25, end=122].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LT) duration 98 frames exceeds threshold 90 frames [start=25, end=122].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (LG) duration 98 frames exceeds threshold 90 frames [start=25, end=122].
- ⚠️ Action 'Action_None' range [22-103] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-160] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-94] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-108] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-97] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-59] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-189] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-210] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-27] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-162] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-201] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-106] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [69-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-108] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-152] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-186] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-25] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-98] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-108] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-62] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-88] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-210] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-32] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-97] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-170] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-27] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [30-44] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-79] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-91] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-132] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-70] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-153] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-149] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-163] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-190] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-200] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-189] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '33' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_293'; source metadata written as null.

</details>