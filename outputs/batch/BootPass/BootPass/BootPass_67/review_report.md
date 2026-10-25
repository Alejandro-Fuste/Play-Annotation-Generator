# Play-Annotation-Generator Annotation Review — BootPass_67

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_67`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `3` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `3` | `3` |
| ❌ MISSING SEGMENT | `Action_BootAway` | TE1 | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_RunFlatRoute` | TE1 | offense | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 15 | START | 14 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `14` | `Group` | 15 | START | 14 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 15 | START | 14 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 15 | START | 14 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 15 | START | 14 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 15 | START | 14 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 15 | START | 14 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 15 | START | 14 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `5` | `Group` | 15 | START | 14 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `6` | `Group` | 15 | START | 14 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 15 | START | 14 | 23 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 24 | START | 24 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `13` | `13` | 27 | START | 39 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `18` | `18` | 27 | START | 27 | 176 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `19` | `19` | 27 | START | 27 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `20` | `20` | 27 | START | 27 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `21` | `21` | 27 | START | 27 | 86 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `3` | 38 | END | 24 | 38 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `3` | `3` | 41 | START | 41 | 67 |
| ❌ MISSING SEGMENT | `Action_BootAway` | TE1 | `15` | `15` | 50 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_RunFlatRoute` | TE1 | `15` | `15` | 78 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 14–193
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 23 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 24 | 38 | 15 | inferred_complete_timeline |
| `Action_None` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_FakeHandoff` | 41 | 67 | 27 | inferred_complete_timeline |
| `Action_None` | 68 | 193 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 14–219
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 23 | 10 | inferred_complete_timeline |
| `Action_None` | 24 | 125 | 102 | inferred_complete_timeline |
| `Action_None` | 137 | 169 | 33 | inferred_complete_timeline |
| `Action_None` | 181 | 187 | 7 | inferred_complete_timeline |
| `Action_None` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_None` | 193 | 203 | 11 | inferred_complete_timeline |
| `Action_None` | 207 | 219 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 14–125
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 23 | 10 | inferred_complete_timeline |
| `Action_None` | 24 | 79 | 56 | inferred_complete_timeline |
| `Action_None` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_None` | 87 | 125 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 14–44
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 44 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 14–306
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 23 | 10 | inferred_complete_timeline |
| `Action_None` | 24 | 306 | 283 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 14–171
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 23 | 10 | inferred_complete_timeline |
| `Action_None` | 24 | 171 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 14–291
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 26 | 13 | inferred_complete_timeline |
| `Action_RunBlock` | 27 | 72 | 46 | inferred_complete_timeline |
| `Action_RunBlock` | 74 | 143 | 70 | inferred_complete_timeline |
| `Action_RunBlock` | 148 | 157 | 10 | inferred_complete_timeline |
| `Action_RunBlock` | 159 | 291 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 14–214
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 26 | 13 | inferred_complete_timeline |
| `Action_RunBlock` | 27 | 86 | 60 | inferred_complete_timeline |
| `Action_RunBlock` | 93 | 95 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 109 | 214 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 14–234
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 23 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 24 | 38 | 15 | inferred_complete_timeline |
| `Action_RunBlock` | 39 | 82 | 44 | inferred_complete_timeline |
| `Action_RunBlock` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 88 | 234 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 14–225
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 26 | 13 | inferred_complete_timeline |
| `Action_RunBlock` | 27 | 176 | 150 | inferred_complete_timeline |
| `Action_RunBlock` | 193 | 225 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 14–215
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 26 | 13 | inferred_complete_timeline |
| `Action_RunBlock` | 27 | 39 | 13 | inferred_complete_timeline |
| `Action_RunBlock` | 51 | 215 | 165 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 14–265
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 23 | 10 | inferred_complete_timeline |
| `Action_None` | 24 | 265 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 14–72
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 23 | 10 | inferred_complete_timeline |
| `Action_None` | 24 | 72 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 14–232
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 23 | 10 | inferred_complete_timeline |
| `Action_None` | 24 | 71 | 48 | inferred_complete_timeline |
| `Action_None` | 88 | 232 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 14–242
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 23 | 10 | inferred_complete_timeline |
| `Action_None` | 24 | 242 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 14–388
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 23 | 10 | inferred_complete_timeline |
| `Action_None` | 24 | 388 | 365 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 14–244
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 23 | 10 | inferred_complete_timeline |
| `Action_None` | 24 | 244 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 14–389
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 23 | 10 | inferred_complete_timeline |
| `Action_None` | 24 | 363 | 340 | inferred_complete_timeline |
| `Action_None` | 367 | 389 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 14–289
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 23 | 10 | inferred_complete_timeline |
| `Action_None` | 24 | 278 | 255 | inferred_complete_timeline |
| `Action_None` | 280 | 289 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 14–348
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 23 | 10 | inferred_complete_timeline |
| `Action_None` | 24 | 348 | 325 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 14–248
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 23 | 10 | inferred_complete_timeline |
| `Action_None` | 24 | 248 | 225 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 14–241 | 228 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 48–53 | 6 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 50–388 | 335 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 70–73 | 4 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 86–324 | 239 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 145–169 | 25 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 147–213 | 41 | 6 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 165–167 | 3 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 190–238 | 49 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 192–283 | 92 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 220–222 | 3 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 235–236 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 287–349 | 63 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (4 segments found)
- ❌ Missing segment for action `Action_BootAway` on target `15` (TE1)
- ❌ Missing segment for action `Action_RunFlatRoute` on target `15` (TE1)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 114: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [24–38], lower_priority='Action_RunBlock' annotated_start=27, effective_Action_RunBlock_start=39.
- ⚠️ Segment 'Action_BootAway' for track '15' has invalid range: start=50, end=44. Clamping end to start.
- ⚠️ Segment 'Action_RunFlatRoute' for track '15' has invalid range: start=78, end=44. Clamping end to start.
- ⚠️ Action 'Action_None' range [24-265] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-241] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-71] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-232] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-193] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-72] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-79] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-125] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-171] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-244] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-125] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-169] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-187] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-203] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-219] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-278] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-289] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-348] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-363] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-248] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [39-82] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [84-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [88-234] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-306] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-242] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-388] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [27-176] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [193-225] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [27-39] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [51-215] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [27-72] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [74-143] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [148-157] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [159-291] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [27-86] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [93-95] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [103-105] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [109-214] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-53] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-378] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-383] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-73] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-324] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-152] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-170] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-213] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-238] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-283] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-349] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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