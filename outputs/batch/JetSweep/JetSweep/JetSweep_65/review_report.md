# Play-Annotation-Generator Annotation Review — JetSweep_65

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_65`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 135
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT2 | defense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `28` | `26` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Toss` | QB | offense | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 188 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 15 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 188 |
| ✅ EXACT | `Action_BallSnap` | DT2 | `7` | `6` | 189 | START | 189 | 201 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `28` | `26` | 194 | START | 218 | 251 |
| ✅ EXACT | `Action_LeadBlock` | TE | `14` | `13` | 194 | START | 194 | 246 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `11` | `10` | 194 | START | 194 | 212 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `5` | `4` | 194 | START | 194 | 202 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `5` | 194 | START | 194 | 246 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `8` | `7` | 194 | START | 194 | 196 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 201 | END | 189 | 201 |
| ✅ EXACT | `Action_Toss` | QB | `9` | `8` | 212 | START | 212 | 219 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `21` | `20` | 220 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 246 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–228
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_SnapReceive` | 189 | 201 | 13 | inferred_complete_timeline |
| `Action_None` | 202 | 211 | 10 | inferred_complete_timeline |
| `Action_Toss` | 212 | 219 | 8 | inferred_complete_timeline |
| `Action_None` | 220 | 222 | 3 | inferred_complete_timeline |
| `Action_None` | 225 | 228 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_None` | 189 | 203 | 15 | inferred_complete_timeline |
| `Action_None` | 210 | 217 | 8 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 234 | 6 | inferred_complete_timeline |
| `Action_None` | 247 | 273 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 15–275
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 193 | 179 | inferred_complete_timeline |
| `Action_LeadBlock` | 194 | 246 | 53 | inferred_complete_timeline |
| `Action_None` | 247 | 260 | 14 | inferred_complete_timeline |
| `Action_None` | 263 | 267 | 5 | inferred_complete_timeline |
| `Action_None` | 273 | 275 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 246 | 53 | inferred_complete_timeline |
| `Action_None` | 247 | 294 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 163 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 212 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 220 | 246 | 27 | inferred_complete_timeline |
| `Action_None` | 247 | 269 | 23 | inferred_complete_timeline |
| `Action_None` | 271 | 281 | 11 | inferred_complete_timeline |
| `Action_None` | 283 | 285 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 202 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 211 | 214 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 193 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 201 | 205 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 228 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 233 | 235 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 237 | 244 | 8 | inferred_complete_timeline |
| `Action_None` | 248 | 250 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–315
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 188 | 67 | inferred_complete_timeline |
| `Action_None` | 189 | 226 | 38 | inferred_complete_timeline |
| `Action_None` | 228 | 310 | 83 | inferred_complete_timeline |
| `Action_None` | 313 | 315 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_None` | 189 | 223 | 35 | inferred_complete_timeline |
| `Action_None` | 229 | 236 | 8 | inferred_complete_timeline |
| `Action_None` | 238 | 242 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–351
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_None` | 189 | 351 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–288
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 188 | 21 | inferred_complete_timeline |
| `Action_BallSnap` | 189 | 201 | 13 | inferred_complete_timeline |
| `Action_None` | 202 | 223 | 22 | inferred_complete_timeline |
| `Action_None` | 225 | 262 | 38 | inferred_complete_timeline |
| `Action_None` | 264 | 288 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 188 | 89 | inferred_complete_timeline |
| `Action_None` | 189 | 197 | 9 | inferred_complete_timeline |
| `Action_None` | 201 | 247 | 47 | inferred_complete_timeline |
| `Action_None` | 259 | 263 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_None` | 189 | 238 | 50 | inferred_complete_timeline |
| `Action_None` | 243 | 252 | 10 | inferred_complete_timeline |
| `Action_None` | 254 | 268 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 27–251 | 193 | 6 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 84–227 | 143 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 99–359 | 251 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 121–151 | 30 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 146–318 | 170 | 5 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 154–159 | 4 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 191–197 | 7 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 198–259 | 50 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 199–259 | 57 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 206–214 | 9 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 214–219 | 6 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 216–240 | 22 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 218–279 | 61 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 228–347 | 118 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 249–257 | 9 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 257–359 | 103 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 258–275 | 18 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 294–359 | 62 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 340–359 | 20 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 343–359 | 17 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 343–358 | 16 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 359–359 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `26` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (5 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `21` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 88 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 132: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '20' has invalid range: start=220, end=197. Clamping end to start.
- ⚠️ Action 'Action_None' range [189-223] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-236] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-242] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-197] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-247] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-263] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-238] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-252] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-268] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-202] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [211-214] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-294] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-166] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-223] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-262] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-288] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-112] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-193] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-196] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [201-205] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [207-228] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [233-235] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [237-244] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-351] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-163] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-212] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-281] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-203] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-217] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-234] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-273] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-226] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-310] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-315] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [194-246] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-260] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-267] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-37] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-76] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-178] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-251] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-120] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-227] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-122] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-222] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-337] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-359] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-148] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-151] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-278] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-290] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-302] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-318] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-155] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-159] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-197] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-207] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-228] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-259] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-244] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-259] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-214] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-219] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-220] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-240] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [218-251] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [253-279] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-336] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-347] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-257] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-275] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-334] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-359] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-359] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-359] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-358] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.

</details>