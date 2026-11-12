# Play-Annotation-Generator Annotation Review — SplitZone_40

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_40`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 144
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | LT | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `6` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 18 | START | 18 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 18 | START | 18 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 18 | START | 18 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 18 | START | 18 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 18 | START | 18 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 18 | START | 18 | 111 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `16` | `15` | 112 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LT | `0` | `0` | 115 | START | 115 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `13` | 115 | START | 115 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `2` | 115 | START | 115 | 153 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `7` | `7` | 115 | START | 115 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | LT | `0` | `0` | 119 | START | 119 | 134 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 123 | END | 112 | 123 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 134 | START | 134 | 152 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `6` | `6` | 153 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 221 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 18–245
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 111 | 94 | inferred_complete_timeline |
| `Action_SnapReceive` | 112 | 123 | 12 | inferred_complete_timeline |
| `Action_None` | 124 | 133 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 134 | 152 | 19 | inferred_complete_timeline |
| `Action_None` | 153 | 187 | 35 | inferred_complete_timeline |
| `Action_None` | 192 | 207 | 16 | inferred_complete_timeline |
| `Action_None` | 235 | 241 | 7 | inferred_complete_timeline |
| `Action_None` | 243 | 245 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 18–149
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 145 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 149 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 18–273
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 70 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 114 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_SplitBlock` | 119 | 134 | 16 | inferred_complete_timeline |
| `Action_SplitBlock` | 168 | 178 | 11 | inferred_complete_timeline |
| `Action_SplitBlock` | 181 | 209 | 29 | inferred_complete_timeline |
| `Action_None` | 233 | 256 | 24 | inferred_complete_timeline |
| `Action_None` | 259 | 273 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 18–237
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 44 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 114 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 129 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 140 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 221 | 69 | inferred_complete_timeline |
| `Action_None` | 222 | 237 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 18–288
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 114 | 97 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 138 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 221 | 54 | inferred_complete_timeline |
| `Action_None` | 222 | 288 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 18–261
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 114 | 97 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 153 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 172 | 221 | 50 | inferred_complete_timeline |
| `Action_None` | 222 | 261 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 18–131
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 111 | 94 | inferred_complete_timeline |
| `Action_None` | 112 | 131 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 18–172
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 111 | 94 | inferred_complete_timeline |
| `Action_None` | 112 | 172 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 18–329
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 44 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 52 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 111 | 49 | inferred_complete_timeline |
| `Action_None` | 112 | 121 | 10 | inferred_complete_timeline |
| `Action_None` | 132 | 178 | 47 | inferred_complete_timeline |
| `Action_None` | 190 | 295 | 106 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |
| `Action_None` | 305 | 310 | 6 | inferred_complete_timeline |
| `Action_None` | 315 | 329 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 18–329
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 57 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 62 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 69 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 110 | 40 | inferred_complete_timeline |
| `Action_None` | 112 | 114 | 3 | inferred_complete_timeline |
| `Action_None` | 149 | 164 | 16 | inferred_complete_timeline |
| `Action_None` | 197 | 227 | 31 | inferred_complete_timeline |
| `Action_None` | 246 | 250 | 5 | inferred_complete_timeline |
| `Action_None` | 252 | 253 | 2 | inferred_complete_timeline |
| `Action_None` | 259 | 272 | 14 | inferred_complete_timeline |
| `Action_None` | 275 | 292 | 18 | inferred_complete_timeline |
| `Action_None` | 294 | 329 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 18–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 111 | 94 | inferred_complete_timeline |
| `Action_None` | 112 | 135 | 24 | inferred_complete_timeline |
| `Action_None` | 138 | 329 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 18–138
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 111 | 94 | inferred_complete_timeline |
| `Action_None` | 112 | 126 | 15 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_None` | 134 | 138 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 18–299
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 111 | 94 | inferred_complete_timeline |
| `Action_None` | 112 | 142 | 31 | inferred_complete_timeline |
| `Action_None` | 198 | 214 | 17 | inferred_complete_timeline |
| `Action_None` | 217 | 219 | 3 | inferred_complete_timeline |
| `Action_None` | 253 | 299 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 37–183
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 111 | 75 | inferred_complete_timeline |
| `Action_None` | 112 | 183 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 18–64 | 46 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 46–71 | 18 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 119–329 | 202 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 125–222 | 57 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 138–227 | 30 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 155–156 | 2 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 158–252 | 92 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 162–197 | 36 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 163–238 | 39 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 165–231 | 63 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 165–226 | 62 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 178–181 | 4 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 185–248 | 7 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 213–219 | 7 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 232–329 | 91 | 3 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 237–308 | 72 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 246–265 | 20 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 248–329 | 73 | 2 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 252–329 | 78 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 261–328 | 66 | 2 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 272–312 | 23 | 2 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 273–278 | 6 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 284–329 | 46 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 297–329 | 32 | 2 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 315–329 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `15` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `0` (3 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `6` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 88 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (RT) duration 107 frames exceeds threshold 90 frames [start=115, end=221].
- ⚠️ Segment 'Action_BallCarry' for track '6' has invalid range: start=153, end=149. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (LG) duration 107 frames exceeds threshold 90 frames [start=115, end=221].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (RG) duration 107 frames exceeds threshold 90 frames [start=115, end=221].
- ⚠️ Segment 'Action_BallSnap' for track '15' has invalid range: start=112, end=71. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [18-70] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-73] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [119-134] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [168-178] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [181-209] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-256] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-273] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-142] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-214] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [115-153] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-261] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-131] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-57] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-64] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-172] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-145] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-44] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [115-129] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-140] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-135] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-187] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-207] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-44] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-52] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-60] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-121] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-178] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-295] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-310] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-111] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-126] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-138] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-57] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-62] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-69] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-164] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-227] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-250] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-272] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-292] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [115-138] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-288] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-183] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-54] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-164] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-315] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-181] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-222] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-156] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-227] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-252] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-197] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-194] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-238] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-225] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-226] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-219] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-311] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-308] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-265] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-302] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-317] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-328] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-287] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-312] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-278] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.

</details>