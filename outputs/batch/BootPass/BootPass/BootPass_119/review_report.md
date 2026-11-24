# Play-Annotation-Generator Annotation Review — BootPass_119

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_119`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 71
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | RT | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_RunBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | RT | offense | `16` | `16` |
| ✅ EXACT | `Action_FakeHandoff` | RT | offense | `16` | `16` |
| ✅ EXACT | `Action_BootAway` | RT | offense | `16` | `16` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | RG | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `17` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 35 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 36 | START | 36 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `14` | `14` | 56 | START | 56 | 151 |
| ❌ MISSING SEGMENT | `Action_RunBlock` | RT | `16` | `16` | 56 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_RunBlock` | C | `19` | `19` | 56 | START | 95 | 97 |
| ✅ EXACT | `Action_RunBlock` | RG | `20` | `20` | 56 | START | 56 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `21` | `21` | 56 | START | 56 | 56 |
| ✅ EXACT | `Action_SnapReceive` | RT | `16` | `16` | 56 | END | 36 | 56 |
| ✅ EXACT | `Action_FakeHandoff` | RT | `16` | `16` | 85 | START | 85 | 95 |
| ✅ EXACT | `Action_BootAway` | RT | `16` | `16` | 96 | START | 96 | 128 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | RG | `20` | `20` | 148 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 164 | 129 | inferred_complete_timeline |
| `Action_None` | 175 | 188 | 14 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_None` | 203 | 204 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 99 | 64 | inferred_complete_timeline |
| `Action_None` | 104 | 269 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 218 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 182 | 147 | inferred_complete_timeline |
| `Action_None` | 185 | 188 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 186 | 151 | inferred_complete_timeline |
| `Action_None` | 188 | 199 | 12 | inferred_complete_timeline |
| `Action_None` | 203 | 249 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 269 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_RunBlock` | 56 | 151 | 96 | inferred_complete_timeline |
| `Action_RunBlock` | 159 | 269 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_RunBlock` | 56 | 56 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 58 | 190 | 133 | inferred_complete_timeline |
| `Action_RunBlock` | 195 | 198 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 202 | 216 | 15 | inferred_complete_timeline |
| `Action_RunBlock` | 218 | 269 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_BallSnap` | 36 | 52 | 17 | inferred_complete_timeline |
| `Action_RunBlock` | 95 | 97 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 55 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 56 | 109 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_SnapReceive` | 36 | 56 | 21 | inferred_complete_timeline |
| `Action_None` | 57 | 84 | 28 | inferred_complete_timeline |
| `Action_FakeHandoff` | 85 | 95 | 11 | inferred_complete_timeline |
| `Action_BootAway` | 96 | 128 | 33 | inferred_complete_timeline |
| `Action_None` | 129 | 269 | 141 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 177 | 142 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 269 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 269 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 99 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 269 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 269 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 195 | 160 | inferred_complete_timeline |
| `Action_None` | 197 | 269 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 211 | 176 | inferred_complete_timeline |
| `Action_None` | 218 | 227 | 10 | inferred_complete_timeline |
| `Action_None` | 230 | 254 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 197 | 162 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 202 | 205 | 4 | inferred_complete_timeline |
| `Action_None` | 207 | 269 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 219 | 184 | inferred_complete_timeline |
| `Action_None` | 221 | 269 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 110 | 75 | inferred_complete_timeline |
| `Action_None` | 112 | 269 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 161 | 126 | inferred_complete_timeline |
| `Action_None` | 163 | 169 | 7 | inferred_complete_timeline |
| `Action_None` | 171 | 209 | 39 | inferred_complete_timeline |
| `Action_None` | 211 | 263 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 116–269 | 154 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 125–269 | 145 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 127–269 | 119 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 219–269 | 43 | 6 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 228–247 | 20 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 254–269 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `14` (2 segments found)
- ❌ Missing segment for action `Action_RunBlock` on target `16` (RT)
- ⚠️ `Action_RunBlock` for actor_track_id `19` (C): Annotated start 56 != Inferred start 95
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (5 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `20` (RG)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF3` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_SecureCatch' at frame 171 targets track ID '39', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Overlapping action conflict at frame 56 for track '16': 'Action_RunBlock' vs 'Action_SnapReceive'. Overriding with 'Action_SnapReceive'.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [36–56], lower_priority='Action_RunBlock' annotated_start=56, effective_Action_RunBlock_start=57.
- ⚠️ Segment 'Action_ThrowPass' for track '20' has invalid range: start=148, end=109. Clamping end to start.
- ⚠️ Action 'Action_None' range [36-182] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-219] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-177] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-195] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-218] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-197] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-99] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-110] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-269] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-99] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-161] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-169] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-209] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-263] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [56-151] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [159-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-211] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-227] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-254] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-186] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-249] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-164] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-188] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [36-52] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [95-97] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [56-109] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' for track '21' starts at frame 56, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_RunBlock' range [56-56] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [58-190] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [195-198] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [202-216] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-138] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-163] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-225] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-246] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-255] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-247] for track '26' has 1 frames without a visible bounding box.
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

</details>