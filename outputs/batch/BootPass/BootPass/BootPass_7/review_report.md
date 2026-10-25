# Play-Annotation-Generator Annotation Review — BootPass_7

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_7`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 71
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_RunFlatRoute` | RB | offense | `13` | `13` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_SecureCatch` | CB2 | defense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `18` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 35 |
| ✅ EXACT | `Action_BallSnap` | LG | `20` | `20` | 36 | START | 36 | 53 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 53 | END | 36 | 53 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `10` | `10` | 58 | START | 58 | 78 |
| ✅ EXACT | `Action_RunFlatRoute` | RB | `13` | `13` | 81 | START | 81 | 117 |
| ✅ EXACT | `Action_BootAway` | QB | `10` | `10` | 82 | START | 82 | 119 |
| ✅ EXACT | `Action_ThrowPass` | QB | `10` | `10` | 135 | START | 135 | 146 |
| ✅ EXACT | `Action_SecureCatch` | CB2 | `11` | `11` | 199 | START | 199 | 204 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_SnapReceive` | 36 | 53 | 18 | inferred_complete_timeline |
| `Action_None` | 54 | 57 | 4 | inferred_complete_timeline |
| `Action_FakeHandoff` | 58 | 78 | 21 | inferred_complete_timeline |
| `Action_None` | 79 | 81 | 3 | inferred_complete_timeline |
| `Action_BootAway` | 82 | 119 | 38 | inferred_complete_timeline |
| `Action_None` | 120 | 134 | 15 | inferred_complete_timeline |
| `Action_ThrowPass` | 135 | 146 | 12 | inferred_complete_timeline |
| `Action_None` | 147 | 194 | 48 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 81 | 117 | 37 | inferred_complete_timeline |
| `Action_None` | 118 | 159 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 116 | 81 | inferred_complete_timeline |
| `Action_None` | 118 | 119 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 299 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 277 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 150 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_BallSnap` | 36 | 53 | 18 | inferred_complete_timeline |
| `Action_None` | 54 | 221 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 47 | 12 | inferred_complete_timeline |
| `Action_None` | 52 | 217 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 131 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 156 | 121 | inferred_complete_timeline |
| `Action_None` | 159 | 161 | 3 | inferred_complete_timeline |
| `Action_None` | 166 | 178 | 13 | inferred_complete_timeline |
| `Action_None` | 180 | 190 | 11 | inferred_complete_timeline |
| `Action_None` | 200 | 204 | 5 | inferred_complete_timeline |
| `Action_None` | 209 | 230 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 72 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 200 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 176 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 233 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 286 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 104 | 69 | inferred_complete_timeline |
| `Action_None` | 112 | 128 | 17 | inferred_complete_timeline |
| `Action_None` | 130 | 187 | 58 | inferred_complete_timeline |
| `Action_None` | 198 | 206 | 9 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 299 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–282
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_SecureCatch` | 199 | 204 | 6 | inferred_complete_timeline |
| `Action_None` | 205 | 282 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 299 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 299 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 299 | 264 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–299 | 300 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–179 | 157 | 12 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 98–109 | 9 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 131–299 | 169 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 135–228 | 88 | 5 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 142–214 | 73 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 186–187 | 2 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 188–228 | 41 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 200–224 | 25 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 6, Column 'Run Block': Could not parse frame number from '-' in entry '-,OL'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 16: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [36-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-72] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-233] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-200] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-286] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-176] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-116] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-178] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-190] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-204] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-230] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-194] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-282] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-104] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-187] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-206] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-47] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-217] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-277] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-131] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-221] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-150] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-67] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-78] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-98] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-118] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-179] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-109] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-190] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-228] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-214] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-228] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-224] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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