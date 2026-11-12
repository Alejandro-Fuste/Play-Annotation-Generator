# Play-Annotation-Generator Annotation Review — SplitZone_109

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_109`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 104
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 96
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `8` | `8` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `19` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 2 | START | 3 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 2 | START | 3 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 2 | START | 3 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `13` | `Group` | 2 | START | 3 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 2 | START | 3 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 2 | START | 3 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 2 | START | 3 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 2 | START | 3 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 2 | START | 3 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 2 | START | 3 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 2 | START | 3 | 92 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `8` | 93 | START | 93 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `18` | 96 | START | 96 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `21` | 96 | START | 96 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `5` | `5` | 96 | START | 96 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `7` | 96 | START | 96 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `8` | `8` | 96 | START | 109 | 114 |
| ✅ EXACT | `Action_SplitBlock` | HB | `13` | `13` | 101 | START | 101 | 208 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 108 | END | 93 | 108 |
| ✅ EXACT | `Action_BallCarry` | QB | `19` | `19` | 137 | START | 137 | 329 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 208 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 3–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 92 | 90 | inferred_complete_timeline |
| `Action_SnapReceive` | 93 | 108 | 16 | inferred_complete_timeline |
| `Action_None` | 109 | 136 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 137 | 329 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 3–114
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 92 | 90 | inferred_complete_timeline |
| `Action_None` | 93 | 114 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 3–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 100 | 98 | inferred_complete_timeline |
| `Action_SplitBlock` | 101 | 208 | 108 | inferred_complete_timeline |
| `Action_None` | 209 | 270 | 62 | inferred_complete_timeline |
| `Action_None` | 272 | 329 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 3–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 92 | 90 | inferred_complete_timeline |
| `Action_None` | 93 | 329 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 3–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 92 | 90 | inferred_complete_timeline |
| `Action_None` | 93 | 211 | 119 | inferred_complete_timeline |
| `Action_None` | 214 | 221 | 8 | inferred_complete_timeline |
| `Action_None` | 223 | 329 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 3–219
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 92 | 90 | inferred_complete_timeline |
| `Action_None` | 93 | 213 | 121 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 3–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 95 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 115 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 208 | 89 | inferred_complete_timeline |
| `Action_None` | 209 | 218 | 10 | inferred_complete_timeline |
| `Action_None` | 223 | 329 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 3–329
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 95 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 115 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 203 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 206 | 208 | 3 | inferred_complete_timeline |
| `Action_None` | 209 | 218 | 10 | inferred_complete_timeline |
| `Action_None` | 220 | 221 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 247 | 24 | inferred_complete_timeline |
| `Action_None` | 249 | 329 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 3–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 92 | 90 | inferred_complete_timeline |
| `Action_BallSnap` | 93 | 108 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 114 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 208 | 89 | inferred_complete_timeline |
| `Action_None` | 209 | 329 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 3–329
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 95 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 115 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 122 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 208 | 68 | inferred_complete_timeline |
| `Action_None` | 209 | 209 | 1 | inferred_complete_timeline |
| `Action_None` | 211 | 215 | 5 | inferred_complete_timeline |
| `Action_None` | 229 | 266 | 38 | inferred_complete_timeline |
| `Action_None` | 268 | 295 | 28 | inferred_complete_timeline |
| `Action_None` | 300 | 329 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 3–203
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 95 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 115 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 169 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 182 | 198 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 201 | 203 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 3–192
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 92 | 90 | inferred_complete_timeline |
| `Action_None` | 93 | 115 | 23 | inferred_complete_timeline |
| `Action_None` | 120 | 192 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 3–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 92 | 90 | inferred_complete_timeline |
| `Action_None` | 93 | 329 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 3–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 92 | 90 | inferred_complete_timeline |
| `Action_None` | 93 | 115 | 23 | inferred_complete_timeline |
| `Action_None` | 119 | 218 | 100 | inferred_complete_timeline |
| `Action_None` | 220 | 274 | 55 | inferred_complete_timeline |
| `Action_None` | 280 | 283 | 4 | inferred_complete_timeline |
| `Action_None` | 285 | 329 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 3–138
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 92 | 90 | inferred_complete_timeline |
| `Action_None` | 93 | 117 | 25 | inferred_complete_timeline |
| `Action_None` | 120 | 138 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 3–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 92 | 90 | inferred_complete_timeline |
| `Action_None` | 93 | 218 | 126 | inferred_complete_timeline |
| `Action_None` | 223 | 240 | 18 | inferred_complete_timeline |
| `Action_None` | 243 | 329 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 3–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 92 | 90 | inferred_complete_timeline |
| `Action_None` | 93 | 216 | 124 | inferred_complete_timeline |
| `Action_None` | 223 | 329 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 3–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 92 | 90 | inferred_complete_timeline |
| `Action_None` | 93 | 329 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 3–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 92 | 90 | inferred_complete_timeline |
| `Action_None` | 93 | 247 | 155 | inferred_complete_timeline |
| `Action_None` | 250 | 295 | 46 | inferred_complete_timeline |
| `Action_None` | 303 | 325 | 23 | inferred_complete_timeline |
| `Action_None` | 327 | 329 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 3–326
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 92 | 90 | inferred_complete_timeline |
| `Action_None` | 93 | 316 | 224 | inferred_complete_timeline |
| `Action_None` | 325 | 326 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 3–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 92 | 90 | inferred_complete_timeline |
| `Action_None` | 93 | 311 | 219 | inferred_complete_timeline |
| `Action_None` | 315 | 329 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 3–273
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 92 | 90 | inferred_complete_timeline |
| `Action_None` | 93 | 241 | 149 | inferred_complete_timeline |
| `Action_None` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_None` | 262 | 273 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 132–329 | 198 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 139–140 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 146–149 | 4 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 173–329 | 139 | 5 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 224–329 | 105 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 230–329 | 98 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 245–247 | 3 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 255–256 | 2 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 270–273 | 4 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 274–329 | 56 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 290–291 | 2 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 303–329 | 11 | 3 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 311–329 | 12 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (LT) duration 113 frames exceeds threshold 90 frames [start=96, end=208].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 108 frames exceeds threshold 90 frames [start=96, end=203].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (C) duration 113 frames exceeds threshold 90 frames [start=96, end=208].
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [93–108], lower_priority='Action_ZoneBlock' annotated_start=96, effective_Action_ZoneBlock_start=109.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (RG) duration 113 frames exceeds threshold 90 frames [start=96, end=208].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 113 frames exceeds threshold 90 frames [start=96, end=208].
- ⚠️ Action 'Action_None' range [93-213] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-211] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-221] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-115] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-218] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-329] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-117] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-138] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-115] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-169] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [174-175] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [182-198] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [201-203] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-311] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-115] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-192] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-218] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-240] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-329] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-114] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-270] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-247] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-295] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-325] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-216] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-218] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-274] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-283] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-241] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-273] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-115] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [137-138] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 209, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [209-209] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-266] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-295] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-316] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-115] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [142-203] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-218] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-247] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-199] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-250] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-318] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-314] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-329] for track '34' has 1 frames without a visible bounding box.
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