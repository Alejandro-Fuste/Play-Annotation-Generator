# Play-Annotation-Generator Annotation Review — InsideZoneRead_174

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_174`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | WR4 | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `16` | `15` |
| ✅ EXACT | `Action_ReadDefender` | RB | offense | `16` | `15` |
| ✅ EXACT | `Action_Handoff` | RB | offense | `16` | `15` |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | RT | offense | `15` | `14` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 2 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 2 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 2 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 2 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 2 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 2 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 2 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 2 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 2 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 2 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `9` | `Group` | 2 | START | 0 | 34 |
| ✅ EXACT | `Action_BallSnap` | WR4 | `9` | `8` | 35 | START | 35 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 38 | START | 38 | 66 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `15` | `14` | 38 | START | 38 | 67 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `18` | `17` | 38 | START | 38 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `19` | 38 | START | 38 | 67 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `7` | 38 | START | 38 | 125 |
| ✅ EXACT | `Action_SnapReceive` | RB | `16` | `15` | 49 | END | 35 | 49 |
| ✅ EXACT | `Action_ReadDefender` | RB | `16` | `15` | 54 | START | 54 | 66 |
| ✅ EXACT | `Action_Handoff` | RB | `16` | `15` | 67 | START | 67 | 84 |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | RT | `15` | `14` | 71 | START | 72 | 125 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `2` | `1` | 85 | START | 85 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 125 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 147 | 113 | inferred_complete_timeline |
| `Action_None` | 150 | 201 | 52 | inferred_complete_timeline |
| `Action_None` | 204 | 269 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_SnapReceive` | 35 | 49 | 15 | inferred_complete_timeline |
| `Action_None` | 50 | 53 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 54 | 66 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 67 | 84 | 18 | inferred_complete_timeline |
| `Action_None` | 85 | 216 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_BallCarry` | 85 | 269 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 269 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 269 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_BallSnap` | 35 | 49 | 15 | inferred_complete_timeline |
| `Action_None` | 50 | 163 | 114 | inferred_complete_timeline |
| `Action_None` | 168 | 269 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 125 | 88 | inferred_complete_timeline |
| `Action_None` | 126 | 130 | 5 | inferred_complete_timeline |
| `Action_None` | 135 | 139 | 5 | inferred_complete_timeline |
| `Action_None` | 141 | 144 | 4 | inferred_complete_timeline |
| `Action_None` | 149 | 269 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 67 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 78 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 66 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 74 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 67 | 30 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 72 | 125 | 54 | inferred_complete_timeline |
| `Action_None` | 126 | 164 | 39 | inferred_complete_timeline |
| `Action_None` | 167 | 269 | 103 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 100 | 66 | inferred_complete_timeline |
| `Action_None` | 102 | 110 | 9 | inferred_complete_timeline |
| `Action_None` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_None` | 154 | 269 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 104 | 70 | inferred_complete_timeline |
| `Action_None` | 107 | 125 | 19 | inferred_complete_timeline |
| `Action_None` | 134 | 198 | 65 | inferred_complete_timeline |
| `Action_None` | 200 | 269 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 80 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 123 | 89 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 159 | 6 | inferred_complete_timeline |
| `Action_None` | 167 | 269 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 217 | 183 | inferred_complete_timeline |
| `Action_None` | 221 | 226 | 6 | inferred_complete_timeline |
| `Action_None` | 228 | 258 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 223 | 189 | inferred_complete_timeline |
| `Action_None` | 226 | 269 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 220 | 186 | inferred_complete_timeline |
| `Action_None` | 223 | 269 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 269 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 132 | 98 | inferred_complete_timeline |
| `Action_None` | 135 | 139 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–269 | 237 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–221 | 205 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 155–193 | 39 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 155–269 | 115 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 156–183 | 16 | 4 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 169–225 | 57 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 173–175 | 3 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 173–269 | 96 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 174–269 | 59 | 9 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 209–269 | 61 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 221–269 | 49 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 252–269 | 18 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ `Action_BlockSecondLevel` for actor_track_id `15` (RT): Annotated start 71 != Inferred start 72

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 348: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [35-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-269] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-100] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-110] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-104] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-125] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-198] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-217] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-226] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-258] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-147] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-201] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-130] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-139] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-163] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-80] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-209] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-123] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-132] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-66] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-67] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [72-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-164] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-216] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-220] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-74] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-159] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-194] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-221] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-67] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-223] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-193] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-269] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-176] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-225] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-203] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-198] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-230] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_174'; source metadata written as null.

</details>