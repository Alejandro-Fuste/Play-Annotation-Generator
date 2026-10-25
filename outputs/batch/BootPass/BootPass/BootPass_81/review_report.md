# Play-Annotation-Generator Annotation Review — BootPass_81

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_81`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 64
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 10
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_RunFlatRoute` | WR2 | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 255 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 124 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 125 | START | 125 | 141 |
| ✅ EXACT | `Action_RunBlock` | LT | `10` | `10` | 134 | START | 134 | 265 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `14` | `14` | 134 | START | 142 | 145 |
| ✅ EXACT | `Action_RunBlock` | LG | `19` | `19` | 134 | START | 134 | 262 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `20` | `20` | 134 | START | 134 | 152 |
| ✅ EXACT | `Action_RunBlock` | RT | `21` | `21` | 134 | START | 134 | 257 |
| ✅ EXACT | `Action_RunFlatRoute` | WR2 | `2` | `2` | 134 | START | 134 | 219 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 141 | END | 125 | 141 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `18` | `18` | 156 | START | 156 | 156 |
| ✅ EXACT | `Action_BootAway` | QB | `18` | `18` | 157 | START | 157 | 195 |
| ✅ EXACT | `Action_ThrowPass` | QB | `18` | `18` | 207 | START | 207 | 219 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `0` | `0` | 256 | START | 256 | 263 |

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
- **Visible Frames:** 0–253
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_SnapReceive` | 125 | 141 | 17 | inferred_complete_timeline |
| `Action_None` | 142 | 155 | 14 | inferred_complete_timeline |
| `Action_FakeHandoff` | 156 | 156 | 1 | inferred_complete_timeline |
| `Action_BootAway` | 157 | 195 | 39 | inferred_complete_timeline |
| `Action_None` | 196 | 206 | 11 | inferred_complete_timeline |
| `Action_ThrowPass` | 207 | 219 | 13 | inferred_complete_timeline |
| `Action_None` | 220 | 253 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 201 | 77 | inferred_complete_timeline |
| `Action_None` | 203 | 244 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 255 | 256 | inferred_complete_timeline |
| `Action_SecureCatch` | 256 | 263 | 8 | inferred_complete_timeline |
| `Action_None` | 264 | 299 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 134 | 219 | 86 | inferred_complete_timeline |
| `Action_None` | 220 | 266 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 289 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 257 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_RunBlock` | 134 | 265 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–262
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_RunBlock` | 134 | 262 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_BallSnap` | 125 | 141 | 17 | inferred_complete_timeline |
| `Action_RunBlock` | 142 | 145 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 151 | 165 | 15 | inferred_complete_timeline |
| `Action_RunBlock` | 169 | 233 | 65 | inferred_complete_timeline |
| `Action_RunBlock` | 241 | 264 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_RunBlock` | 134 | 152 | 19 | inferred_complete_timeline |
| `Action_RunBlock` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 165 | 170 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_RunBlock` | 134 | 257 | 124 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 256 | 132 | inferred_complete_timeline |
| `Action_None` | 258 | 262 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 147 | 23 | inferred_complete_timeline |
| `Action_None` | 150 | 152 | 3 | inferred_complete_timeline |
| `Action_None` | 154 | 264 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 161 | 37 | inferred_complete_timeline |
| `Action_None` | 165 | 177 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 268 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 267 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 254 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 195 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 280 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 189 | 65 | inferred_complete_timeline |
| `Action_None` | 192 | 230 | 39 | inferred_complete_timeline |
| `Action_None` | 233 | 283 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 175–177 | 3 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 177–258 | 78 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 177–261 | 83 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 180–182 | 3 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 197–200 | 4 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 208–209 | 2 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 213–261 | 49 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 241–243 | 3 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 270–275 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `20` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [125–141], lower_priority='Action_RunBlock' annotated_start=134, effective_Action_RunBlock_start=142.
- ⚠️ Action 'Action_None' range [125-289] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-266] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-256] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-268] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-257] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-280] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-161] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-177] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [134-265] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-195] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-201] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-244] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-254] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [125-141] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [142-145] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [151-165] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [169-233] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [241-264] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-189] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-230] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-283] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-267] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-147] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-264] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-253] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [134-262] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [134-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [158-161] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [165-170] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [134-257] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-185] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-258] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-261] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-261] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-275] for track '30' has 1 frames without a visible bounding box.
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