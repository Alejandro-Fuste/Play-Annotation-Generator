# Play-Annotation-Generator Annotation Review — InsideZoneRead_215

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_215`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 1
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `17` | `15` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `17` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 3 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 48 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `20` | `17` | 46 | START | 169 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `10` | 49 | START | 49 | 99 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `12` | `11` | 49 | START | 49 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `6` | `5` | 49 | START | 49 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `7` | `6` | 49 | START | 49 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `9` | `8` | 49 | START | 49 | 106 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `17` | `15` | 61 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `17` | `15` | 70 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `17` | `15` | 101 | START | 150 | 240 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 120 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 77 | 32 | inferred_complete_timeline |
| `Action_None` | 79 | 83 | 5 | inferred_complete_timeline |
| `Action_None` | 88 | 129 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 3–166
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 48 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 120 | 72 | inferred_complete_timeline |
| `Action_None` | 121 | 158 | 38 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 87 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 113 | 22 | inferred_complete_timeline |
| `Action_None` | 138 | 162 | 25 | inferred_complete_timeline |
| `Action_None` | 164 | 299 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 120 | 72 | inferred_complete_timeline |
| `Action_None` | 121 | 189 | 69 | inferred_complete_timeline |
| `Action_None` | 195 | 204 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 99 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 106 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 120 | 12 | inferred_complete_timeline |
| `Action_None` | 121 | 198 | 78 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 231 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 175 | 130 | inferred_complete_timeline |
| `Action_None` | 184 | 195 | 12 | inferred_complete_timeline |
| `Action_None` | 198 | 207 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 73 | 28 | inferred_complete_timeline |
| `Action_None` | 76 | 299 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 181 | 136 | inferred_complete_timeline |
| `Action_None` | 188 | 198 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 172 | 127 | inferred_complete_timeline |
| `Action_None` | 189 | 212 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–145 | 146 | 2 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 112–140 | 29 | 1 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 124–129 | 6 | 1 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 145–190 | 46 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 150–299 | 138 | 4 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 163–299 | 102 | 3 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 169–173 | 5 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 170–299 | 128 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 179–263 | 84 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 179–299 | 121 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 186–214 | 29 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 190–299 | 110 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 212–299 | 85 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 220–299 | 67 | 4 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 226–271 | 43 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 228–299 | 65 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 229–299 | 65 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 250–299 | 50 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 293–299 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `20` (Position_Unknown): Annotated start 46 != Inferred start 169
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `17` (Position_Unknown)
- ❌ Missing segment for action `Action_ReadDefender` on target `17` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (4 segments found)

### Track Identity Issues

- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 4 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_SnapReceive' for track '15' has invalid range: start=150, end=61. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '15' has invalid range: start=150, end=100. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '17' has invalid range: start=169, end=61. Clamping end to start.
- ⚠️ Action 'Action_None' range [46-181] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-198] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-231] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-175] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-195] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-207] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-73] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-172] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-212] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-189] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-204] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-87] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-113] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-162] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-299] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-145] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-106] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-198] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '9' starts at frame 46, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [46-77] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-83] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-129] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-99] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-48] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-140] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-190] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [150-240] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [242-260] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [271-285] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-186] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-290] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-274] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-212] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-263] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-214] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-299] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-256] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-276] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-245] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-271] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-281] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-277] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_215'; source metadata written as null.

</details>