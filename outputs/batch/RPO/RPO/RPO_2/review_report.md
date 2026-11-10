# Play-Annotation-Generator Annotation Review — RPO_2

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_2`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 29
- **Ball Tracks:** 1
- **Action Segments:** 83
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `18` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `2` | `2` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `3` | `3` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `5` | `5` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBall` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `10` | `10` | 85 | START | 85 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `12` | `12` | 85 | START | 85 | 94 |
| ✅ EXACT | `Action_RunBlock` | RG | `2` | `2` | 85 | START | 85 | 104 |
| ✅ EXACT | `Action_RunBlock` | RT | `3` | `3` | 85 | START | 85 | 113 |
| ✅ EXACT | `Action_RunBlock` | LG | `5` | `5` | 85 | START | 85 | 148 |
| ✅ EXACT | `Action_ReadDefender` | QB | `14` | `14` | 113 | START | 113 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBall` | QB | `14` | `14` | 120 | START | 120 | 123 |
| ✅ EXACT | `Action_ThrowPass` | QB | `14` | `14` | 139 | START | 139 | 148 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 32 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 83 | 43 | inferred_complete_timeline |
| `Action_None` | 84 | 112 | 29 | inferred_complete_timeline |
| `Action_ReadDefender` | 113 | 119 | 7 | inferred_complete_timeline |
| `Action_PullBall` | 120 | 123 | 4 | inferred_complete_timeline |
| `Action_PullBall` | 129 | 138 | 10 | inferred_complete_timeline |
| `Action_ThrowPass` | 139 | 148 | 10 | inferred_complete_timeline |
| `Action_None` | 149 | 176 | 28 | inferred_complete_timeline |
| `Action_None` | 178 | 195 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 178 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 201 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 84 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 85 | 95 | 11 | inferred_complete_timeline |
| `Action_RunBlock` | 97 | 129 | 33 | inferred_complete_timeline |
| `Action_RunBlock` | 132 | 143 | 12 | inferred_complete_timeline |
| `Action_RunBlock` | 146 | 148 | 3 | inferred_complete_timeline |
| `Action_None` | 149 | 214 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 84 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 85 | 148 | 64 | inferred_complete_timeline |
| `Action_None` | 149 | 203 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 84 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 85 | 94 | 10 | inferred_complete_timeline |
| `Action_RunBlock` | 105 | 148 | 44 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 203 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 84 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 85 | 104 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 84 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 85 | 113 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 190 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 106 | 23 | inferred_complete_timeline |
| `Action_None` | 109 | 115 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 124 | 41 | inferred_complete_timeline |
| `Action_None` | 133 | 149 | 17 | inferred_complete_timeline |
| `Action_None` | 154 | 171 | 18 | inferred_complete_timeline |
| `Action_None` | 175 | 183 | 9 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 269 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 203 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 186 | 103 | inferred_complete_timeline |
| `Action_None` | 191 | 193 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 199 | 116 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 122–128 | 5 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 134–269 | 134 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 138–269 | 102 | 6 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 141–203 | 62 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 143–269 | 92 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 153–269 | 117 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 166–167 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 168–269 | 102 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 178–209 | 27 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 200–206 | 7 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 207–260 | 51 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 218–269 | 52 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 221–269 | 49 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 234–235 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | 106 | 115 | 7 | 70.0% | 108–110 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `10` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBall` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 53 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [84-199] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-186] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [85-104] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [85-113] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-190] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-203] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-203] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-178] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-106] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-115] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [85-95] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [97-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [132-143] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-214] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-201] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [85-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-203] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-124] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-171] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-183] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-32] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-39] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-83] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 84, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [84-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBall' range [120-123] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-176] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-195] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-265] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-147] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-213] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-233] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-199] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-213] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-187] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-209] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-250] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-260] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '29' has 1 frames without a visible bounding box.
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

</details>