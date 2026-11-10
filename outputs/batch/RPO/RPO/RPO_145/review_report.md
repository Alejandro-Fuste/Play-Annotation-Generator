# Play-Annotation-Generator Annotation Review — RPO_145

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_145`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunHitchRoute` | actor_track_id `19` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_PullBall` | RB | offense | `10` | `10` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `19` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 43 |
| ✅ EXACT | `Action_ZoneBlock` | C | `17` | `17` | 45 | START | 45 | 112 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `18` | `18` | 45 | START | 45 | 112 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `20` | `20` | 45 | START | 45 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `21` | 45 | START | 45 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `8` | `8` | 45 | START | 45 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | `16` | `16` | 59 | START | 59 | 106 |
| ✅ EXACT | `Action_PullBall` | RB | `10` | `10` | 81 | START | 81 | 88 |
| ✅ EXACT | `Action_ThrowPass` | RB | `10` | `10` | 105 | START | 105 | 112 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 58 | 15 | inferred_complete_timeline |
| `Action_ReadDefender` | 59 | 106 | 48 | inferred_complete_timeline |
| `Action_ReadDefender` | 109 | 269 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 80 | 37 | inferred_complete_timeline |
| `Action_PullBall` | 81 | 88 | 8 | inferred_complete_timeline |
| `Action_None` | 89 | 104 | 16 | inferred_complete_timeline |
| `Action_ThrowPass` | 105 | 112 | 8 | inferred_complete_timeline |
| `Action_None` | 113 | 269 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 269 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 269 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 269 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 112 | 68 | inferred_complete_timeline |
| `Action_None` | 113 | 269 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 57 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 112 | 37 | inferred_complete_timeline |
| `Action_None` | 113 | 125 | 13 | inferred_complete_timeline |
| `Action_None` | 135 | 269 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 112 | 68 | inferred_complete_timeline |
| `Action_None` | 113 | 269 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 112 | 68 | inferred_complete_timeline |
| `Action_None` | 113 | 202 | 90 | inferred_complete_timeline |
| `Action_None` | 205 | 207 | 3 | inferred_complete_timeline |
| `Action_None` | 209 | 269 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 107 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 112 | 4 | inferred_complete_timeline |
| `Action_None` | 113 | 175 | 63 | inferred_complete_timeline |
| `Action_None` | 177 | 202 | 26 | inferred_complete_timeline |
| `Action_None` | 205 | 207 | 3 | inferred_complete_timeline |
| `Action_None` | 210 | 227 | 18 | inferred_complete_timeline |
| `Action_None` | 230 | 232 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 85 | 42 | inferred_complete_timeline |
| `Action_None` | 92 | 269 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 118 | 75 | inferred_complete_timeline |
| `Action_None` | 120 | 125 | 6 | inferred_complete_timeline |
| `Action_None` | 129 | 167 | 39 | inferred_complete_timeline |
| `Action_None` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 269 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 102 | 59 | inferred_complete_timeline |
| `Action_None` | 109 | 118 | 10 | inferred_complete_timeline |
| `Action_None` | 120 | 269 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 268 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 269 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 237 | 194 | inferred_complete_timeline |
| `Action_None` | 239 | 269 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 269 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 269 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 147 | 104 | inferred_complete_timeline |
| `Action_None` | 154 | 159 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 269 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 189 | 146 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–102 | 101 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 103–104 | 2 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 116–268 | 121 | 10 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 130–269 | 140 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 160–161 | 2 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 189–204 | 16 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 226–269 | 40 | 3 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 240–269 | 30 | 1 | Undefined position; Undefined team |
| `29` | `46` | Position_Unknown | Team_Unknown | 257–264 | 4 | 2 | Undefined position; Undefined team |
| `30` | `48` | Position_Unknown | Team_Unknown | 263–264 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 264: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [44-92] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-102] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-85] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-118] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-125] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-167] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-269] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-189] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-237] for track '6' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-147] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-107] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-175] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-202] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-227] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-268] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [59-106] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [109-269] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-269] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-112] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-202] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '21' starts at frame 45, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [45-48] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-57] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-68] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-269] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-126] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-152] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-181] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-199] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-259] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-268] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-204] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>