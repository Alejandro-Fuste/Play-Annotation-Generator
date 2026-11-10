# Play-Annotation-Generator Annotation Review — RPO_65

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_65`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunHitchRoute` | actor_track_id `3` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `13` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `12` | 65 | START | 65 | 78 |
| ✅ EXACT | `Action_ZoneBlock` | C | `16` | `16` | 65 | START | 65 | 74 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `17` | `17` | 65 | START | 65 | 106 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `20` | `20` | 65 | START | 65 | 106 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `21` | 65 | START | 65 | 106 |
| ✅ EXACT | `Action_ReadDefender` | QB | `19` | `19` | 72 | START | 72 | 83 |
| ✅ EXACT | `Action_PullBall` | QB | `19` | `19` | 84 | START | 84 | 91 |
| ✅ EXACT | `Action_ThrowPass` | QB | `19` | `19` | 98 | START | 98 | 106 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 71 | 8 | inferred_complete_timeline |
| `Action_ReadDefender` | 72 | 83 | 12 | inferred_complete_timeline |
| `Action_PullBall` | 84 | 91 | 8 | inferred_complete_timeline |
| `Action_None` | 92 | 97 | 6 | inferred_complete_timeline |
| `Action_ThrowPass` | 98 | 106 | 9 | inferred_complete_timeline |
| `Action_None` | 107 | 137 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 83 | 20 | inferred_complete_timeline |
| `Action_None` | 88 | 153 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 129 | 66 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 132 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 75 | 12 | inferred_complete_timeline |
| `Action_None` | 78 | 116 | 39 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 64 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 106 | 42 | inferred_complete_timeline |
| `Action_None` | 107 | 154 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 64 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 106 | 42 | inferred_complete_timeline |
| `Action_None` | 107 | 153 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 64 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 74 | 10 | inferred_complete_timeline |
| `Action_None` | 114 | 165 | 52 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 64 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 106 | 42 | inferred_complete_timeline |
| `Action_None` | 107 | 120 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 64 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 78 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 84 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 106 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 74 | 11 | inferred_complete_timeline |
| `Action_None` | 79 | 84 | 6 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 153 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 102 | 39 | inferred_complete_timeline |
| `Action_None` | 110 | 146 | 37 | inferred_complete_timeline |
| `Action_None` | 148 | 155 | 8 | inferred_complete_timeline |
| `Action_None` | 159 | 163 | 5 | inferred_complete_timeline |
| `Action_None` | 168 | 170 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 75 | 12 | inferred_complete_timeline |
| `Action_None` | 77 | 108 | 32 | inferred_complete_timeline |
| `Action_None` | 110 | 129 | 20 | inferred_complete_timeline |
| `Action_None` | 131 | 149 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 111 | 48 | inferred_complete_timeline |
| `Action_None` | 113 | 152 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 152 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 76 | 13 | inferred_complete_timeline |
| `Action_None` | 78 | 107 | 30 | inferred_complete_timeline |
| `Action_None` | 113 | 143 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 130 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 141 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 212 | 149 | inferred_complete_timeline |
| `Action_None` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_None` | 223 | 269 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 106 | 43 | inferred_complete_timeline |
| `Action_None` | 110 | 226 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 225 | 162 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |
| `Action_None` | 230 | 263 | 34 | inferred_complete_timeline |
| `Action_None` | 266 | 269 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–165 | 160 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 134–199 | 66 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 168–264 | 90 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 169–172 | 4 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 169–173 | 5 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 234–269 | 36 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 245–257 | 7 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 247–267 | 13 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 248–269 | 22 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 255–269 | 9 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 259–260 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 261–269 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 120: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [64-132] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-130] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-141] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-155] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-212] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-76] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-107] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-75] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-108] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-111] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-152] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-74] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-84] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-153] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-226] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-225] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-263] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-152] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-78] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-84] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-83] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-153] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-102] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-146] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-163] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-74] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-165] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-120] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-75] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-116] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-137] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-106] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-154] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-106] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-153] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-223] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-233] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-253] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-249] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-252] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-267] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>