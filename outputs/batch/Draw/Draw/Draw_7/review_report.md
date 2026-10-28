# Play-Annotation-Generator Annotation Review — Draw_7

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_7`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 60
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 51
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `6` | `5` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `11` | `10` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `21` | `20` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 57 |
| ✅ EXACT | `Action_BallSnap` | C | `6` | `5` | 58 | START | 58 | 75 |
| ✅ EXACT | `Action_PassBlock` | RT | `11` | `10` | 61 | START | 61 | 136 |
| ✅ EXACT | `Action_PassBlock` | RG | `16` | `15` | 61 | START | 61 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `19` | 61 | START | 61 | 136 |
| ✅ EXACT | `Action_PassBlock` | LT | `21` | `20` | 61 | START | 61 | 136 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `6` | `5` | 61 | START | 86 | 136 |
| ✅ EXACT | `Action_SnapReceive` | QB | `22` | `21` | 75 | END | 58 | 75 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `22` | `21` | 83 | START | 83 | 103 |
| ✅ EXACT | `Action_BallCarry` | QB | `22` | `21` | 104 | START | 104 | 115 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 136 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_SnapReceive` | 58 | 75 | 18 | inferred_complete_timeline |
| `Action_None` | 76 | 82 | 7 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 83 | 103 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 104 | 115 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 106 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 246 | 189 | inferred_complete_timeline |
| `Action_None` | 251 | 255 | 5 | inferred_complete_timeline |
| `Action_None` | 257 | 329 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 241 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 252 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 120 | 63 | inferred_complete_timeline |
| `Action_None` | 125 | 329 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PassBlock` | 61 | 136 | 76 | inferred_complete_timeline |
| `Action_None` | 137 | 257 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PassBlock` | 61 | 136 | 76 | inferred_complete_timeline |
| `Action_None` | 137 | 285 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–309
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_BallSnap` | 58 | 75 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 86 | 136 | 51 | inferred_complete_timeline |
| `Action_None` | 137 | 245 | 109 | inferred_complete_timeline |
| `Action_None` | 247 | 309 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PassBlock` | 61 | 85 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PassBlock` | 61 | 136 | 76 | inferred_complete_timeline |
| `Action_None` | 137 | 207 | 71 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 278 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 250 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 112 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 226 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–279
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 103 | 46 | inferred_complete_timeline |
| `Action_None` | 107 | 241 | 135 | inferred_complete_timeline |
| `Action_None` | 244 | 279 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 178 | 121 | inferred_complete_timeline |
| `Action_None` | 182 | 329 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 133 | 76 | inferred_complete_timeline |
| `Action_None` | 139 | 321 | 183 | inferred_complete_timeline |
| `Action_None` | 323 | 329 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 329 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–261
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 261 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 283 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–317
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 317 | 260 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 2–12 | 11 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 81–260 | 156 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 114–329 | 178 | 6 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 121–329 | 205 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 134–275 | 141 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 197–198 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `6` (C): Annotated start 61 != Inferred start 86

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [58–75], lower_priority='Action_PassBlock' annotated_start=61, effective_Action_PassBlock_start=76.
- ⚠️ Action 'Action_None' range [58-252] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-241] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-120] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-261] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-246] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-255] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [58-75] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-245] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-309] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-329] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-278] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-178] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-283] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [61-136] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-207] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-241] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-279] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-250] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-317] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [61-85] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-226] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-321] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-329] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-106] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [61-136] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-285] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [61-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-257] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [104-115] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-12] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-147] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-260] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-130] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-142] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-246] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-289] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-329] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-275] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '27' has 1 frames without a visible bounding box.
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