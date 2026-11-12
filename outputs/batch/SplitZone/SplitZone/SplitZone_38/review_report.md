# Play-Annotation-Generator Annotation Review — SplitZone_38

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_38`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `16` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 103 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 101 | START | 101 | 111 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `12` | `12` | 104 | START | 104 | 115 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `15` | `15` | 104 | START | 112 | 199 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `4` | 104 | START | 104 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `5` | `5` | 104 | START | 104 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `7` | 104 | START | 104 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `2` | `2` | 107 | START | 107 | 168 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 111 | END | 101 | 111 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `10` | 123 | START | 123 | 148 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `16` | `16` | 149 | START | 149 | 216 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 199 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_SnapReceive` | 101 | 111 | 11 | inferred_complete_timeline |
| `Action_None` | 112 | 122 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 123 | 148 | 26 | inferred_complete_timeline |
| `Action_None` | 149 | 207 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 135 | 35 | inferred_complete_timeline |
| `Action_None` | 138 | 142 | 5 | inferred_complete_timeline |
| `Action_None` | 148 | 182 | 35 | inferred_complete_timeline |
| `Action_None` | 185 | 188 | 4 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_None` | 202 | 207 | 6 | inferred_complete_timeline |
| `Action_None` | 209 | 252 | 44 | inferred_complete_timeline |
| `Action_None` | 259 | 299 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 299 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_SplitBlock` | 107 | 168 | 62 | inferred_complete_timeline |
| `Action_SplitBlock` | 175 | 191 | 17 | inferred_complete_timeline |
| `Action_SplitBlock` | 193 | 199 | 7 | inferred_complete_timeline |
| `Action_None` | 200 | 202 | 3 | inferred_complete_timeline |
| `Action_None` | 204 | 273 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 115 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 118 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 149 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_BallSnap` | 101 | 111 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 199 | 88 | inferred_complete_timeline |
| `Action_None` | 200 | 209 | 10 | inferred_complete_timeline |
| `Action_None` | 220 | 228 | 9 | inferred_complete_timeline |
| `Action_None` | 239 | 299 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 145 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 199 | 49 | inferred_complete_timeline |
| `Action_None` | 200 | 299 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 156 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 199 | 4 | inferred_complete_timeline |
| `Action_None` | 200 | 299 | 100 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 106 | 6 | inferred_complete_timeline |
| `Action_None` | 111 | 299 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 121 | 21 | inferred_complete_timeline |
| `Action_None` | 147 | 299 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 112 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 153 | 53 | inferred_complete_timeline |
| `Action_None` | 167 | 186 | 20 | inferred_complete_timeline |
| `Action_None` | 200 | 218 | 19 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 238 | 15 | inferred_complete_timeline |
| `Action_None` | 248 | 251 | 4 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 147 | 47 | inferred_complete_timeline |
| `Action_None` | 208 | 214 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 125 | 25 | inferred_complete_timeline |
| `Action_None` | 127 | 219 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 188 | 88 | inferred_complete_timeline |
| `Action_None` | 205 | 235 | 31 | inferred_complete_timeline |
| `Action_None` | 239 | 280 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 119–299 | 177 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 123–136 | 14 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 162–222 | 50 | 3 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 174–279 | 103 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 192–227 | 34 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 240–297 | 58 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 241–299 | 59 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 247–299 | 53 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 254–299 | 46 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 254–299 | 39 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 256–299 | 40 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 257–299 | 34 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 258–299 | 42 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `15` (C): Annotated start 104 != Inferred start 112
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (RG) duration 96 frames exceeds threshold 90 frames [start=104, end=199].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 96 frames exceeds threshold 90 frames [start=104, end=199].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (C) duration 96 frames exceeds threshold 90 frames [start=104, end=199].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [101–111], lower_priority='Action_ZoneBlock' annotated_start=104, effective_Action_ZoneBlock_start=112.
- ⚠️ Action 'Action_None' range [101-188] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-235] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-280] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [107-168] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [175-191] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-273] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-186] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-218] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-238] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-145] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-118] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-149] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-182] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-252] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-299] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-156] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-147] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-214] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-121] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-299] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-207] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-125] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-219] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-115] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-112] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-209] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-228] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [149-216] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-202] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-211] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-274] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-216] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-227] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-297] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-261] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-278] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-291] for track '27' has 2 frames without a visible bounding box.
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

</details>