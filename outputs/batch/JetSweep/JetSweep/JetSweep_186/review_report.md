# Play-Annotation-Generator Annotation Review — JetSweep_186

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_186`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 115
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | Team_Unknown | `21` | `19` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE2 | offense | `3` | `2` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Toss` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 94 |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | `21` | `19` | 67 | START | 88 | 120 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 95 | START | 95 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE2 | `3` | `2` | 96 | START | 96 | 192 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `10` | `9` | 96 | START | 110 | 213 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `14` | `13` | 96 | START | 96 | 211 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `17` | 96 | START | 96 | 199 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 96 | START | 96 | 202 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `5` | 96 | START | 96 | 199 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 109 | END | 95 | 109 |
| ✅ EXACT | `Action_Toss` | QB | `9` | `8` | 119 | START | 119 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `21` | `19` | 121 | START | 121 | 205 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 242 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_SnapReceive` | 95 | 109 | 15 | inferred_complete_timeline |
| `Action_None` | 110 | 118 | 9 | inferred_complete_timeline |
| `Action_Toss` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 213 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 225 | 131 | inferred_complete_timeline |
| `Action_None` | 231 | 276 | 46 | inferred_complete_timeline |
| `Action_None` | 278 | 329 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–316
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 213 | 119 | inferred_complete_timeline |
| `Action_None` | 222 | 316 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_LeadBlock` | 96 | 192 | 97 | inferred_complete_timeline |
| `Action_LeadBlock` | 224 | 236 | 13 | inferred_complete_timeline |
| `Action_LeadBlock` | 242 | 242 | 1 | inferred_complete_timeline |
| `Action_None` | 243 | 246 | 4 | inferred_complete_timeline |
| `Action_None` | 250 | 329 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 202 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 199 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_BallSnap` | 95 | 109 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 213 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 211 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 199 | 104 | inferred_complete_timeline |
| `Action_ZoneBlock` | 201 | 202 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 132 | 38 | inferred_complete_timeline |
| `Action_None` | 135 | 138 | 4 | inferred_complete_timeline |
| `Action_None` | 140 | 143 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 180 | 86 | inferred_complete_timeline |
| `Action_None` | 182 | 278 | 97 | inferred_complete_timeline |
| `Action_None` | 303 | 329 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 99 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 103 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 114 | 20 | inferred_complete_timeline |
| `Action_None` | 117 | 180 | 64 | inferred_complete_timeline |
| `Action_None` | 182 | 259 | 78 | inferred_complete_timeline |
| `Action_None` | 263 | 274 | 12 | inferred_complete_timeline |
| `Action_None` | 276 | 293 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 188 | 94 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 203 | 204 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 94 | 28 | inferred_complete_timeline |
| `Action_None` | 95 | 95 | 1 | inferred_complete_timeline |
| `Action_None` | 101 | 124 | 24 | inferred_complete_timeline |
| `Action_None` | 126 | 205 | 80 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |
| `Action_None` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_None` | 215 | 218 | 4 | inferred_complete_timeline |
| `Action_None` | 222 | 234 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 153 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–309
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 192 | 98 | inferred_complete_timeline |
| `Action_None` | 194 | 254 | 61 | inferred_complete_timeline |
| `Action_None` | 262 | 267 | 6 | inferred_complete_timeline |
| `Action_None` | 276 | 290 | 15 | inferred_complete_timeline |
| `Action_None` | 292 | 295 | 4 | inferred_complete_timeline |
| `Action_None` | 305 | 309 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 135 | 41 | inferred_complete_timeline |
| `Action_None` | 137 | 184 | 48 | inferred_complete_timeline |
| `Action_None` | 186 | 189 | 4 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `21` | Position_Unknown | Team_Unknown | 88–265 | 151 | 6 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 105–206 | 98 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 121–132 | 11 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 145–329 | 185 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 156–210 | 53 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 163–178 | 15 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 176–178 | 3 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 181–329 | 142 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 208–216 | 9 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 217–309 | 86 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 219–224 | 6 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 226–228 | 3 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 229–327 | 99 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 246–329 | 84 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 255–329 | 75 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 310–329 | 20 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_JetMotion` for actor_track_id `21` (Position_Unknown): Annotated start 67 != Inferred start 88
- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `3` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `10` (C): Annotated start 96 != Inferred start 110
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 75 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (LT) duration 107 frames exceeds threshold 90 frames [start=96, end=202].
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '2' (TE2) duration 147 frames exceeds threshold 90 frames [start=96, end=242].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (LG) duration 104 frames exceeds threshold 90 frames [start=96, end=199].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (C) duration 118 frames exceeds threshold 90 frames [start=96, end=213].
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [95–109], lower_priority='Action_ZoneBlock' annotated_start=96, effective_Action_ZoneBlock_start=110.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (RG) duration 116 frames exceeds threshold 90 frames [start=96, end=211].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (RT) duration 107 frames exceeds threshold 90 frames [start=96, end=202].
- ⚠️ Action 'Action_None' range [95-132] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-202] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [96-192] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [224-236] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-246] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-213] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-316] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-188] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-153] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-114] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-180] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-259] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-274] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-293] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-213] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-213] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-225] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-276] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-329] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-99] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-135] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-184] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-211] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 95, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [95-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-124] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-205] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-234] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-192] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-254] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-267] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-290] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-309] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-103] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [201-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-278] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [121-205] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [212-216] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [220-234] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [236-241] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [259-265] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-135] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-206] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-129] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-172] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-201] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-178] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-187] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-216] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-289] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-309] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-224] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-327] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>