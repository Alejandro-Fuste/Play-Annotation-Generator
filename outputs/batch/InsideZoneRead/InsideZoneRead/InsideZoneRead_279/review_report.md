# Play-Annotation-Generator Annotation Review — InsideZoneRead_279

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_279`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB1 | defense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `20` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `21` | `20` |
| ✅ EXACT | `Action_Keep` | QB | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `21` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `22` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_BallSnap` | CB1 | `11` | `10` | 14 | START | 14 | 31 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `9` | 17 | START | 17 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `17` | `16` | 17 | START | 17 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `18` | `17` | 17 | START | 17 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `19` | 17 | START | 17 | 59 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `20` | 31 | END | 14 | 31 |
| ✅ EXACT | `Action_ReadDefender` | QB | `21` | `20` | 36 | START | 36 | 39 |
| ✅ EXACT | `Action_Keep` | QB | `21` | `20` | 40 | START | 40 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `21` | `20` | 60 | START | 60 | 66 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 91 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_SnapReceive` | 14 | 31 | 18 | inferred_complete_timeline |
| `Action_None` | 32 | 35 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 36 | 39 | 4 | inferred_complete_timeline |
| `Action_Keep` | 40 | 59 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 60 | 66 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 73 | 76 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 38 | 25 | inferred_complete_timeline |
| `Action_None` | 44 | 48 | 5 | inferred_complete_timeline |
| `Action_None` | 53 | 167 | 115 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 194 | 181 | inferred_complete_timeline |
| `Action_None` | 202 | 207 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 65 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 91 | 9 | inferred_complete_timeline |
| `Action_None` | 92 | 200 | 109 | inferred_complete_timeline |
| `Action_None` | 202 | 210 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 59 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 91 | 13 | inferred_complete_timeline |
| `Action_None` | 92 | 99 | 8 | inferred_complete_timeline |
| `Action_None` | 105 | 153 | 49 | inferred_complete_timeline |
| `Action_None` | 160 | 169 | 10 | inferred_complete_timeline |
| `Action_None` | 179 | 182 | 4 | inferred_complete_timeline |
| `Action_None` | 184 | 210 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 90 | 74 | inferred_complete_timeline |
| `Action_None` | 98 | 114 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 91 | 75 | inferred_complete_timeline |
| `Action_None` | 92 | 183 | 92 | inferred_complete_timeline |
| `Action_None` | 186 | 207 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 49 | 36 | inferred_complete_timeline |
| `Action_None` | 53 | 210 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 74 | 61 | inferred_complete_timeline |
| `Action_None` | 76 | 80 | 5 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_None` | 91 | 153 | 63 | inferred_complete_timeline |
| `Action_None` | 157 | 169 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 44 | 31 | inferred_complete_timeline |
| `Action_None` | 49 | 209 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 76 | 63 | inferred_complete_timeline |
| `Action_None` | 109 | 110 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 114 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_BallSnap` | 14 | 31 | 18 | inferred_complete_timeline |
| `Action_None` | 32 | 42 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 186 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–161 | 162 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 29–30 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 63–126 | 13 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 68–210 | 126 | 4 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 70–207 | 119 | 5 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 94–210 | 104 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 114–116 | 3 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 115–116 | 2 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 127–210 | 84 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 130–210 | 81 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 135–137 | 3 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 154–160 | 7 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 164–165 | 2 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 170–194 | 24 | 2 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 188–209 | 17 | 3 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 190–210 | 15 | 2 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 558: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [14-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-74] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-80] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-153] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-169] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-44] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-209] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-194] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-114] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-183] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-207] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-42] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-76] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-161] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-90] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-114] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-65] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-200] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-49] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-59] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-99] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-153] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-169] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [60-66] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [73-76] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-38] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-48] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-30] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-71] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-126] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-72] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-107] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-178] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-93] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-129] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-207] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-153] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-175] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-160] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-191] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-209] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-200] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>