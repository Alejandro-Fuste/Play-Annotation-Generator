# Play-Annotation-Generator Annotation Review — RPO_143

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_143`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunHitchRoute` | actor_track_id `1` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_PullBall` | RB | offense | `5` | `5` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 20 | START | 20 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 20 | START | 20 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 20 | START | 20 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 20 | START | 20 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 20 | START | 20 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 20 | START | 20 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 20 | START | 20 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 20 | START | 20 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 20 | START | 20 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 20 | START | 20 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 20 | START | 20 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `15` | 40 | START | 40 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `17` | 40 | START | 40 | 47 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `19` | `19` | 40 | START | 40 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `20` | 40 | START | 40 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 40 | START | 40 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | `9` | `9` | 50 | START | 50 | 172 |
| ✅ EXACT | `Action_PullBall` | RB | `5` | `5` | 62 | START | 62 | 70 |
| ✅ EXACT | `Action_ThrowPass` | RB | `5` | `5` | 83 | START | 83 | 89 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 20–239
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 49 | 11 | inferred_complete_timeline |
| `Action_ReadDefender` | 50 | 172 | 123 | inferred_complete_timeline |
| `Action_ReadDefender` | 176 | 239 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 20–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 61 | 23 | inferred_complete_timeline |
| `Action_PullBall` | 62 | 70 | 9 | inferred_complete_timeline |
| `Action_None` | 71 | 82 | 12 | inferred_complete_timeline |
| `Action_ThrowPass` | 83 | 89 | 7 | inferred_complete_timeline |
| `Action_None` | 90 | 239 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 20–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 239 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 20–239
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 181 | 143 | inferred_complete_timeline |
| `Action_None` | 186 | 239 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 20–217
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 213 | 175 | inferred_complete_timeline |
| `Action_None` | 216 | 217 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 20–115
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 115 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 20–239
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 39 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 51 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 63 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 88 | 3 | inferred_complete_timeline |
| `Action_None` | 93 | 239 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 20–76
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 39 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 47 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 76 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 20–239
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 39 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 44 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 89 | 43 | inferred_complete_timeline |
| `Action_None` | 90 | 239 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 20–87
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 39 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 49 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 58 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 76 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 87 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 20–51
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 39 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 51 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 20–239
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 103 | 65 | inferred_complete_timeline |
| `Action_None` | 105 | 107 | 3 | inferred_complete_timeline |
| `Action_None` | 110 | 239 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 20–117
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 117 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 20–239
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 76 | 38 | inferred_complete_timeline |
| `Action_None` | 97 | 182 | 86 | inferred_complete_timeline |
| `Action_None` | 186 | 188 | 3 | inferred_complete_timeline |
| `Action_None` | 190 | 199 | 10 | inferred_complete_timeline |
| `Action_None` | 214 | 239 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 20–64
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 61 | 23 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 20–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 162 | 124 | inferred_complete_timeline |
| `Action_None` | 164 | 239 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 20–239
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 117 | 79 | inferred_complete_timeline |
| `Action_None` | 119 | 123 | 5 | inferred_complete_timeline |
| `Action_None` | 128 | 239 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 20–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 200 | 162 | inferred_complete_timeline |
| `Action_None` | 202 | 239 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 20–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 239 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 20–230
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 230 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 20–239
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 185 | 147 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 197 | 239 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 20–239
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 190 | 152 | inferred_complete_timeline |
| `Action_None` | 195 | 239 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 52–84 | 33 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 55–239 | 184 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 72–119 | 23 | 6 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 74–239 | 164 | 2 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 89–239 | 143 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 116–239 | 123 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 129–239 | 109 | 2 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 133–239 | 107 | 1 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 133–134 | 2 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 196–239 | 38 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 56 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [39-181] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-61] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-117] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-200] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-103] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-115] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-213] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [50-172] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [176-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-185] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-190] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-230] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-76] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-199] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-47] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [75-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-117] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-239] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-51] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-51] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [53-63] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-80] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-88] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-49] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-58] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-76] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-87] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-84] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-64] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-239] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-77] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-90] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-111] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-203] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-216] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-146] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-224] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-239] for track '31' has 5 frames without a visible bounding box.
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

</details>