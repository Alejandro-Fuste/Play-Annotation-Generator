# Play-Annotation-Generator Annotation Review — SplitZone_309

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_309`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 60
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | SAF2 | defense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `14` | `14` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_PressEdge` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | DE1 | defense | `10` | `10` |
| ✅ EXACT | `Action_ReadEdgeDefender` | DE1 | defense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | DE1 | defense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | C | offense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `17` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `20` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `21` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 45 |
| ✅ EXACT | `Action_BallSnap` | RG | `14` | `14` | 46 | START | 46 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | SAF2 | `15` | `15` | 56 | START | 56 | 58 |
| ✅ EXACT | `Action_ZoneBlock` | C | `11` | `11` | 56 | START | 56 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `14` | `14` | 56 | START | 56 | 71 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LG | `17` | `17` | 56 | START | 107 | 107 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `4` | `4` | 56 | START | 56 | 104 |
| ✅ EXACT | `Action_PressEdge` | C | `11` | `11` | 60 | START | 60 | 90 |
| ✅ EXACT | `Action_SnapReceive` | DE1 | `10` | `10` | 60 | END | 46 | 60 |
| ✅ EXACT | `Action_ReadEdgeDefender` | DE1 | `10` | `10` | 69 | START | 69 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | DE1 | `10` | `10` | 83 | START | 83 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | C | `11` | `11` | 91 | START | 91 | 107 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 133–139
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 133 | 139 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 136–148
- **Visible Samples:** 12

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 136 | 138 | 3 | inferred_complete_timeline |
| `Action_None` | 140 | 148 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 262 | 217 | inferred_complete_timeline |
| `Action_None` | 265 | 274 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 128 | 83 | inferred_complete_timeline |
| `Action_None` | 130 | 160 | 31 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 168 | 173 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 175 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 116 | 71 | inferred_complete_timeline |
| `Action_None` | 130 | 169 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 107–160
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 107 | 107 | 1 | inferred_complete_timeline |
| `Action_None` | 108 | 160 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 59 | 4 | inferred_complete_timeline |
| `Action_PressEdge` | 60 | 90 | 31 | inferred_complete_timeline |
| `Action_BallCarry` | 91 | 107 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 110 | 262 | 153 | inferred_complete_timeline |
| `Action_BallCarry` | 264 | 299 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_BallSnap` | 46 | 55 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 71 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 104 | 32 | inferred_complete_timeline |
| `Action_None` | 105 | 225 | 121 | inferred_complete_timeline |
| `Action_None` | 229 | 233 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 104 | 49 | inferred_complete_timeline |
| `Action_None` | 105 | 299 | 195 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_SnapReceive` | 46 | 60 | 15 | inferred_complete_timeline |
| `Action_None` | 61 | 68 | 8 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 69 | 82 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 89 | 93 | 5 | inferred_complete_timeline |
| `Action_None` | 94 | 220 | 127 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 299 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 96 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 155 | 110 | inferred_complete_timeline |
| `Action_None` | 157 | 205 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 45 | 15 | inferred_complete_timeline |
| `Action_None` | 46 | 212 | 167 | inferred_complete_timeline |
| `Action_None` | 215 | 218 | 4 | inferred_complete_timeline |
| `Action_None` | 220 | 264 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 139 | 94 | inferred_complete_timeline |
| `Action_None` | 148 | 299 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 74–299
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 74 | 299 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 73 | 28 | inferred_complete_timeline |
| `Action_None` | 75 | 77 | 3 | inferred_complete_timeline |
| `Action_None` | 115 | 134 | 20 | inferred_complete_timeline |
| `Action_None` | 137 | 207 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 65 | 20 | inferred_complete_timeline |
| `Action_None` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_None` | 99 | 102 | 4 | inferred_complete_timeline |
| `Action_None` | 110 | 164 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 128–248
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 128 | 248 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_SplitBlock` | 56 | 58 | 3 | inferred_complete_timeline |
| `Action_SplitBlock` | 61 | 65 | 5 | inferred_complete_timeline |
| `Action_SplitBlock` | 67 | 95 | 29 | inferred_complete_timeline |
| `Action_None` | 96 | 299 | 204 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 157–158 | 2 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 180–243 | 64 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 204–219 | 15 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 269–272 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `17` (LG): Annotated start 56 != Inferred start 107
- ⚠️ Ambiguous match for action `Action_Handoff` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 4 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 4 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 8 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '17' has invalid range: start=107, end=104. Clamping end to start.
- ⚠️ Action 'Action_None' range [46-139] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-116] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-169] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-175] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-128] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-160] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-173] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-96] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-262] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-274] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-65] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-102] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-164] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-212] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-264] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [46-60] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [83-85] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-220] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [91-107] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [110-262] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-73] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-134] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-207] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-155] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-205] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-104] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-225] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-233] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [56-58] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [61-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [67-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-160] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-248] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-139] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-148] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-243] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-211] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-219] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.

</details>