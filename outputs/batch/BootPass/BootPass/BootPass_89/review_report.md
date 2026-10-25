# Play-Annotation-Generator Annotation Review — BootPass_89

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_89`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `21` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `21` | `21` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `21` | `21` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `21` | `21` |
| ✅ EXACT | `Action_SecureCatch` | RB | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 68 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 64 | START | 64 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `13` | `13` | 69 | START | 69 | 176 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `18` | `18` | 69 | START | 79 | 93 |
| ✅ EXACT | `Action_RunBlock` | RG | `19` | `19` | 69 | START | 69 | 299 |
| ✅ EXACT | `Action_RunBlock` | RT | `20` | `20` | 69 | START | 69 | 299 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `8` | `8` | 69 | START | 69 | 176 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `21` | 78 | END | 64 | 78 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `21` | `21` | 90 | START | 90 | 94 |
| ✅ EXACT | `Action_BootAway` | QB | `21` | `21` | 95 | START | 95 | 165 |
| ✅ EXACT | `Action_ThrowPass` | QB | `21` | `21` | 166 | START | 166 | 175 |
| ✅ EXACT | `Action_SecureCatch` | RB | `14` | `14` | 207 | START | 207 | 219 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 63 | 60 | inferred_complete_timeline |
| `Action_SnapReceive` | 64 | 78 | 15 | inferred_complete_timeline |
| `Action_None` | 79 | 89 | 11 | inferred_complete_timeline |
| `Action_FakeHandoff` | 90 | 94 | 5 | inferred_complete_timeline |
| `Action_BootAway` | 95 | 165 | 71 | inferred_complete_timeline |
| `Action_ThrowPass` | 166 | 175 | 10 | inferred_complete_timeline |
| `Action_None` | 176 | 299 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 206 | 29 | inferred_complete_timeline |
| `Action_SecureCatch` | 207 | 219 | 13 | inferred_complete_timeline |
| `Action_None` | 220 | 229 | 10 | inferred_complete_timeline |
| `Action_None` | 232 | 235 | 4 | inferred_complete_timeline |
| `Action_None` | 243 | 296 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 140 | 77 | inferred_complete_timeline |
| `Action_None` | 149 | 160 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 132 | 69 | inferred_complete_timeline |
| `Action_None` | 137 | 195 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 160 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 173 | 110 | inferred_complete_timeline |
| `Action_None` | 181 | 297 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_RunBlock` | 69 | 176 | 108 | inferred_complete_timeline |
| `Action_RunBlock` | 178 | 216 | 39 | inferred_complete_timeline |
| `Action_RunBlock` | 227 | 299 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_RunBlock` | 69 | 176 | 108 | inferred_complete_timeline |
| `Action_RunBlock` | 181 | 299 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_BallSnap` | 64 | 78 | 15 | inferred_complete_timeline |
| `Action_RunBlock` | 79 | 93 | 15 | inferred_complete_timeline |
| `Action_RunBlock` | 98 | 99 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_RunBlock` | 69 | 299 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_RunBlock` | 69 | 299 | 231 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 101 | 38 | inferred_complete_timeline |
| `Action_None` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_None` | 111 | 113 | 3 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 129 | 3 | inferred_complete_timeline |
| `Action_None` | 137 | 142 | 6 | inferred_complete_timeline |
| `Action_None` | 145 | 159 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 100 | 37 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_None` | 105 | 299 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 73 | 10 | inferred_complete_timeline |
| `Action_None` | 77 | 85 | 9 | inferred_complete_timeline |
| `Action_None` | 94 | 299 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 81 | 18 | inferred_complete_timeline |
| `Action_None` | 89 | 102 | 14 | inferred_complete_timeline |
| `Action_None` | 105 | 107 | 3 | inferred_complete_timeline |
| `Action_None` | 111 | 115 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 240 | 177 | inferred_complete_timeline |
| `Action_None` | 244 | 250 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 230 | 167 | inferred_complete_timeline |
| `Action_None` | 232 | 299 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–285
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 148 | 85 | inferred_complete_timeline |
| `Action_None` | 154 | 212 | 59 | inferred_complete_timeline |
| `Action_None` | 215 | 250 | 36 | inferred_complete_timeline |
| `Action_None` | 252 | 253 | 2 | inferred_complete_timeline |
| `Action_None` | 255 | 257 | 3 | inferred_complete_timeline |
| `Action_None` | 260 | 285 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 114 | 51 | inferred_complete_timeline |
| `Action_None` | 124 | 128 | 5 | inferred_complete_timeline |
| `Action_None` | 132 | 163 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 141 | 78 | inferred_complete_timeline |
| `Action_None` | 145 | 299 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 226 | 163 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_None` | 232 | 241 | 10 | inferred_complete_timeline |
| `Action_None` | 244 | 253 | 10 | inferred_complete_timeline |
| `Action_None` | 255 | 299 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–189 | 184 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 99–137 | 36 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 100–205 | 100 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 150–299 | 142 | 5 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 158–268 | 98 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 186–289 | 46 | 5 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 217–299 | 81 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 264–299 | 36 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [64–78], lower_priority='Action_RunBlock' annotated_start=69, effective_Action_RunBlock_start=79.
- ⚠️ Action 'Action_None' range [64-160] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-226] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-241] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-253] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-114] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-128] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-163] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-132] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-195] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-140] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-160] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-100] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-240] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-250] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [69-176] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [178-216] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-142] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-159] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-230] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-148] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-212] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-250] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-285] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [69-176] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-176] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-229] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-296] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-73] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-85] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-81] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-102] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-173] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-297] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [79-93] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [98-99] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-63] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-137] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-108] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-205] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-168] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-227] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-246] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-269] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-240] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-254] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-214] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-224] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-249] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-299] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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

</details>