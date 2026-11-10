# Play-Annotation-Generator Annotation Review — RPO_209

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_209`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunInRoute` | actor_track_id `0` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `20` | `20` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 47 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `11` | `11` | 49 | START | 49 | 103 |
| ✅ EXACT | `Action_ZoneBlock` | C | `15` | `15` | 49 | START | 49 | 103 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `17` | `17` | 49 | START | 49 | 103 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `18` | `18` | 49 | START | 49 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 49 | START | 49 | 67 |
| ✅ EXACT | `Action_PullBall` | QB | `20` | `20` | 67 | START | 67 | 77 |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | QB | `20` | `20` | 67 | START | N/A | N/A |
| ✅ EXACT | `Action_ThrowPass` | QB | `20` | `20` | 94 | START | 94 | 103 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 66 | 19 | inferred_complete_timeline |
| `Action_PullBall` | 67 | 77 | 11 | inferred_complete_timeline |
| `Action_None` | 78 | 93 | 16 | inferred_complete_timeline |
| `Action_ThrowPass` | 94 | 103 | 10 | inferred_complete_timeline |
| `Action_None` | 104 | 269 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 147 | 100 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_None` | 170 | 178 | 9 | inferred_complete_timeline |
| `Action_None` | 181 | 183 | 3 | inferred_complete_timeline |
| `Action_None` | 187 | 269 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 269 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 269 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 269 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 227 | 180 | inferred_complete_timeline |
| `Action_None` | 232 | 234 | 3 | inferred_complete_timeline |
| `Action_None` | 244 | 263 | 20 | inferred_complete_timeline |
| `Action_None` | 265 | 269 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 48 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 103 | 55 | inferred_complete_timeline |
| `Action_None` | 104 | 143 | 40 | inferred_complete_timeline |
| `Action_None` | 146 | 148 | 3 | inferred_complete_timeline |
| `Action_None` | 150 | 152 | 3 | inferred_complete_timeline |
| `Action_None` | 154 | 156 | 3 | inferred_complete_timeline |
| `Action_None` | 176 | 178 | 3 | inferred_complete_timeline |
| `Action_None` | 181 | 183 | 3 | inferred_complete_timeline |
| `Action_None` | 185 | 269 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 48 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 103 | 55 | inferred_complete_timeline |
| `Action_None` | 104 | 106 | 3 | inferred_complete_timeline |
| `Action_None` | 183 | 185 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 48 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 103 | 55 | inferred_complete_timeline |
| `Action_None` | 104 | 135 | 32 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 48 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 67 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 71 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 48 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 103 | 55 | inferred_complete_timeline |
| `Action_None` | 104 | 141 | 38 | inferred_complete_timeline |
| `Action_None` | 145 | 168 | 24 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 97 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 143 | 96 | inferred_complete_timeline |
| `Action_None` | 145 | 149 | 5 | inferred_complete_timeline |
| `Action_None` | 218 | 222 | 5 | inferred_complete_timeline |
| `Action_None` | 226 | 232 | 7 | inferred_complete_timeline |
| `Action_None` | 234 | 269 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 79 | 32 | inferred_complete_timeline |
| `Action_None` | 82 | 130 | 49 | inferred_complete_timeline |
| `Action_None` | 132 | 135 | 4 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 158 | 269 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 144 | 97 | inferred_complete_timeline |
| `Action_None` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 161 | 10 | inferred_complete_timeline |
| `Action_None` | 165 | 269 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 269 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 269 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 237 | 190 | inferred_complete_timeline |
| `Action_None` | 240 | 257 | 18 | inferred_complete_timeline |
| `Action_None` | 264 | 269 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 129 | 82 | inferred_complete_timeline |
| `Action_None` | 132 | 240 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 269 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 269 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 269 | 222 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 82–87 | 5 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 86–96 | 7 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 103–106 | 4 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 119–139 | 11 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 123–144 | 16 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 158–269 | 101 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 165–269 | 104 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 166–269 | 102 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 173–175 | 3 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 182–269 | 88 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 188–192 | 5 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 188–266 | 16 | 7 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 228–232 | 5 | 1 | Undefined position; Undefined team |
| `35` | `55` | Position_Unknown | Team_Unknown | 257–258 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ❌ Missing segment for action `Action_ReadDefender` on target `20` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Overlapping action conflict at frame 67 for track '20': 'Action_ReadDefender' vs 'Action_PullBall'. Overriding with 'Action_PullBall'.
- ⚠️ Action 'Action_None' range [48-227] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-263] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-143] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-222] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-232] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-144] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-161] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-129] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-240] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-237] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-257] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-141] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-168] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-269] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-79] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-130] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-269] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-269] for track '16' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-143] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-147] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-178] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-67] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-84] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-90] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-126] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-144] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-184] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-192] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '35' has 1 frames without a visible bounding box.
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

</details>