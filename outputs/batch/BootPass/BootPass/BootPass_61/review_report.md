# Play-Annotation-Generator Annotation Review — BootPass_61

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_61`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_RunBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_RunFlatRoute` | RB2 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | RB2 | offense | `1` | `1` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `27` | `25` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `0` | `Group` | 37 | START | 37 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `1` | `Group` | 37 | START | 37 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 37 | START | 37 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 37 | START | 37 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 37 | START | 37 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 37 | START | 37 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 37 | START | 37 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 37 | START | 37 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 37 | START | 37 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 37 | START | 37 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 37 | START | 37 | 57 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 58 | START | 58 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `11` | `11` | 68 | START | 68 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `16` | `16` | 68 | START | 68 | 87 |
| ⚠️ START CHANGED | `Action_RunBlock` | C | `17` | `17` | 68 | START | 75 | 82 |
| ✅ EXACT | `Action_RunBlock` | LG | `20` | `20` | 68 | START | 68 | 321 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `21` | `21` | 68 | START | 68 | 101 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 74 | END | 58 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | QB | `14` | `14` | 80 | START | 80 | 97 |
| ✅ EXACT | `Action_BootAway` | QB | `14` | `14` | 102 | START | 102 | 137 |
| ✅ EXACT | `Action_RunFlatRoute` | RB2 | `1` | `1` | 114 | START | 114 | 137 |
| ✅ EXACT | `Action_ThrowPass` | RB2 | `1` | `1` | 138 | START | 138 | 143 |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `27` | `25` | 195 | START | 195 | 201 |

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
- **Visible Frames:** 37–182
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 57 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 58 | 74 | 17 | inferred_complete_timeline |
| `Action_None` | 75 | 79 | 5 | inferred_complete_timeline |
| `Action_FakeHandoff` | 80 | 97 | 18 | inferred_complete_timeline |
| `Action_FakeHandoff` | 101 | 101 | 1 | inferred_complete_timeline |
| `Action_BootAway` | 102 | 137 | 36 | inferred_complete_timeline |
| `Action_None` | 138 | 182 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 37–282
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 57 | 21 | inferred_complete_timeline |
| `Action_None` | 58 | 282 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 37–329
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 113 | 77 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 114 | 137 | 24 | inferred_complete_timeline |
| `Action_ThrowPass` | 138 | 143 | 6 | inferred_complete_timeline |
| `Action_None` | 144 | 329 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 37–320
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 57 | 21 | inferred_complete_timeline |
| `Action_None` | 58 | 298 | 241 | inferred_complete_timeline |
| `Action_None` | 302 | 320 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 37–121
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 57 | 21 | inferred_complete_timeline |
| `Action_None` | 58 | 121 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 37–329
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 57 | 21 | inferred_complete_timeline |
| `Action_None` | 58 | 90 | 33 | inferred_complete_timeline |
| `Action_None` | 101 | 329 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 37–329
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 67 | 31 | inferred_complete_timeline |
| `Action_RunBlock` | 68 | 101 | 34 | inferred_complete_timeline |
| `Action_RunBlock` | 105 | 329 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 37–321
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 67 | 31 | inferred_complete_timeline |
| `Action_RunBlock` | 68 | 321 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 37–82
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 57 | 21 | inferred_complete_timeline |
| `Action_BallSnap` | 58 | 74 | 17 | inferred_complete_timeline |
| `Action_RunBlock` | 75 | 82 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 37–313
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 67 | 31 | inferred_complete_timeline |
| `Action_RunBlock` | 68 | 87 | 20 | inferred_complete_timeline |
| `Action_RunBlock` | 98 | 313 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 37–315
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 67 | 31 | inferred_complete_timeline |
| `Action_RunBlock` | 68 | 123 | 56 | inferred_complete_timeline |
| `Action_RunBlock` | 128 | 315 | 188 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 37–329
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 57 | 21 | inferred_complete_timeline |
| `Action_None` | 58 | 81 | 24 | inferred_complete_timeline |
| `Action_None` | 90 | 102 | 13 | inferred_complete_timeline |
| `Action_None` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_None` | 111 | 329 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 37–199
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 57 | 21 | inferred_complete_timeline |
| `Action_None` | 58 | 96 | 39 | inferred_complete_timeline |
| `Action_None` | 100 | 199 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 37–93
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 57 | 21 | inferred_complete_timeline |
| `Action_None` | 58 | 93 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 37–323
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 57 | 21 | inferred_complete_timeline |
| `Action_None` | 58 | 102 | 45 | inferred_complete_timeline |
| `Action_None` | 107 | 143 | 37 | inferred_complete_timeline |
| `Action_None` | 146 | 149 | 4 | inferred_complete_timeline |
| `Action_None` | 156 | 158 | 3 | inferred_complete_timeline |
| `Action_None` | 162 | 323 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 37–329
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 57 | 21 | inferred_complete_timeline |
| `Action_None` | 58 | 329 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 37–329
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 57 | 21 | inferred_complete_timeline |
| `Action_None` | 58 | 329 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 37–329
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 57 | 21 | inferred_complete_timeline |
| `Action_None` | 58 | 326 | 269 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 37–236
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 57 | 21 | inferred_complete_timeline |
| `Action_None` | 58 | 236 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 37–329
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 57 | 21 | inferred_complete_timeline |
| `Action_None` | 58 | 115 | 58 | inferred_complete_timeline |
| `Action_None` | 117 | 278 | 162 | inferred_complete_timeline |
| `Action_None` | 283 | 318 | 36 | inferred_complete_timeline |
| `Action_None` | 320 | 329 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 37–329
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 57 | 21 | inferred_complete_timeline |
| `Action_None` | 58 | 329 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 37–302
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 57 | 21 | inferred_complete_timeline |
| `Action_None` | 58 | 127 | 70 | inferred_complete_timeline |
| `Action_None` | 130 | 143 | 14 | inferred_complete_timeline |
| `Action_None` | 145 | 152 | 8 | inferred_complete_timeline |
| `Action_None` | 154 | 167 | 14 | inferred_complete_timeline |
| `Action_None` | 213 | 296 | 84 | inferred_complete_timeline |
| `Action_None` | 298 | 302 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 117–276 | 143 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 149–178 | 30 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 169–329 | 161 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 193–316 | 123 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 274–329 | 56 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 312–327 | 16 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 314–321 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `16` (2 segments found)
- ⚠️ `Action_RunBlock` for actor_track_id `17` (C): Annotated start 68 != Inferred start 75
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_FakeHandoff` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [58–74], lower_priority='Action_RunBlock' annotated_start=68, effective_Action_RunBlock_start=75.
- ⚠️ Action 'Action_None' range [58-282] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-298] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-320] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-102] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-143] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-323] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-90] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-329] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-121] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-127] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-143] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-152] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-167] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-296] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-302] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-236] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [68-123] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [128-315] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-115] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-278] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-318] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-93] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [80-97] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-96] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-199] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [68-87] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [98-313] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [75-82] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-326] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-81] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-102] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [68-321] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [68-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-138] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-236] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-276] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-178] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-329] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-305] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-316] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-329] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-327] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-321] for track '28' has 1 frames without a visible bounding box.
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