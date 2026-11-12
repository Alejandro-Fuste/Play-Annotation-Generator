# Play-Annotation-Generator Annotation Review — SplitZone_107

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_107`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 51
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `14` | `14` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB1 | defense | `5` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 8 | START | 9 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 8 | START | 9 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 8 | START | 9 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 8 | START | 9 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 8 | START | 9 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 8 | START | 9 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 8 | START | 9 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 8 | START | 9 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 8 | START | 9 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 8 | START | 9 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 8 | START | 9 | 103 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 104 | START | 104 | 114 |
| ✅ EXACT | `Action_SplitBlock` | TE | `1` | `1` | 106 | START | 106 | 213 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `13` | 107 | START | 107 | 213 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `14` | `14` | 107 | START | 107 | 213 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `20` | `20` | 107 | START | 115 | 213 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `21` | `21` | 107 | START | 107 | 213 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `6` | 107 | START | 107 | 213 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 114 | END | 104 | 114 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `16` | 119 | START | 119 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB1 | `5` | `5` | 130 | START | 130 | 139 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 213 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_SnapReceive` | 104 | 114 | 11 | inferred_complete_timeline |
| `Action_None` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 119 | 129 | 11 | inferred_complete_timeline |
| `Action_None` | 130 | 299 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 9–289
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_None` | 104 | 156 | 53 | inferred_complete_timeline |
| `Action_None` | 159 | 282 | 124 | inferred_complete_timeline |
| `Action_None` | 288 | 289 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_None` | 104 | 299 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_None` | 104 | 299 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 9–295
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_None` | 104 | 244 | 141 | inferred_complete_timeline |
| `Action_None` | 250 | 257 | 8 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_None` | 263 | 271 | 9 | inferred_complete_timeline |
| `Action_None` | 284 | 285 | 2 | inferred_complete_timeline |
| `Action_None` | 294 | 295 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 105 | 97 | inferred_complete_timeline |
| `Action_SplitBlock` | 106 | 213 | 108 | inferred_complete_timeline |
| `Action_None` | 214 | 299 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 106 | 98 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 213 | 107 | inferred_complete_timeline |
| `Action_None` | 214 | 299 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 106 | 98 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 213 | 107 | inferred_complete_timeline |
| `Action_None` | 214 | 299 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_BallSnap` | 104 | 114 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 213 | 99 | inferred_complete_timeline |
| `Action_None` | 214 | 299 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 106 | 98 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 213 | 107 | inferred_complete_timeline |
| `Action_None` | 214 | 299 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 9–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 106 | 98 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 213 | 107 | inferred_complete_timeline |
| `Action_None` | 214 | 227 | 14 | inferred_complete_timeline |
| `Action_None` | 229 | 232 | 4 | inferred_complete_timeline |
| `Action_None` | 248 | 299 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 9–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_None` | 104 | 227 | 124 | inferred_complete_timeline |
| `Action_None` | 229 | 299 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 9–235
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_None` | 104 | 227 | 124 | inferred_complete_timeline |
| `Action_None` | 232 | 235 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 9–126
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_None` | 104 | 126 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 9–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 129 | 121 | inferred_complete_timeline |
| `Action_BallCarry` | 130 | 139 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 142 | 269 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 9–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_None` | 104 | 211 | 108 | inferred_complete_timeline |
| `Action_None` | 217 | 299 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_None` | 104 | 299 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_None` | 104 | 299 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 9–157
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_None` | 104 | 157 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 9–279
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_None` | 104 | 270 | 167 | inferred_complete_timeline |
| `Action_None` | 275 | 279 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 9–185
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_None` | 104 | 185 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 9–276
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_None` | 104 | 276 | 173 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 130–299 | 141 | 6 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 159–299 | 138 | 3 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 240–299 | 60 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 252–299 | 39 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `20` (C): Annotated start 107 != Inferred start 115
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 4 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 4 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 8 |
| Missing visible bounding boxes during action | 36 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (LT) duration 107 frames exceeds threshold 90 frames [start=107, end=213].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (RT) duration 107 frames exceeds threshold 90 frames [start=107, end=213].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (LG) duration 107 frames exceeds threshold 90 frames [start=107, end=213].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (C) duration 107 frames exceeds threshold 90 frames [start=107, end=213].
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [104–114], lower_priority='Action_ZoneBlock' annotated_start=107, effective_Action_ZoneBlock_start=115.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 107 frames exceeds threshold 90 frames [start=107, end=213].
- ⚠️ Action 'Action_None' range [104-244] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-257] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-271] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-270] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-279] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-126] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-211] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [130-139] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [142-269] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-276] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-185] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-157] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-227] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-227] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-156] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-282] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-227] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-206] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-243] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-255] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-246] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-288] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-299] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-264] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>