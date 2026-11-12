# Play-Annotation-Generator Annotation Review — SplitZone_302

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_302`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 127
- **Validation Warnings:** 132
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 105
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `1` | `1` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `6` | `6` |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `24` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `27` | `24` |
| ❌ MISSING SEGMENT | `Action_Handoff` | RB | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `14` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `19` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 119 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 111 | START | 111 | 124 |
| ✅ EXACT | `Action_SplitBlock` | TE | `1` | `1` | 116 | START | 116 | 161 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `15` | `15` | 120 | START | 125 | 146 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `17` | `17` | 120 | START | 120 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `20` | 120 | START | 120 | 140 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `21` | 120 | START | 120 | 180 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `9` | `9` | 120 | START | 120 | 180 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 124 | END | 111 | 124 |
| ✅ EXACT | `Action_PressEdge` | RB | `6` | `6` | 126 | START | 126 | 155 |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | `24` | `22` | 149 | START | 149 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `27` | `24` | 157 | START | 157 | 195 |
| ❌ MISSING SEGMENT | `Action_Handoff` | RB | `6` | `6` | 187 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_SnapReceive` | 111 | 124 | 14 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_PressEdge` | 126 | 155 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 299 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 251 | 141 | inferred_complete_timeline |
| `Action_None` | 256 | 299 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 299 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_SplitBlock` | 116 | 161 | 46 | inferred_complete_timeline |
| `Action_None` | 170 | 299 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 140 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 150 | 9 | inferred_complete_timeline |
| `Action_None` | 212 | 213 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 264 | 48 | inferred_complete_timeline |
| `Action_None` | 269 | 271 | 3 | inferred_complete_timeline |
| `Action_None` | 273 | 275 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 180 | 61 | inferred_complete_timeline |
| `Action_None` | 181 | 203 | 23 | inferred_complete_timeline |
| `Action_None` | 207 | 216 | 10 | inferred_complete_timeline |
| `Action_None` | 221 | 235 | 15 | inferred_complete_timeline |
| `Action_None` | 237 | 299 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_BallSnap` | 111 | 124 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 146 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 134 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 180 | 61 | inferred_complete_timeline |
| `Action_None` | 181 | 193 | 13 | inferred_complete_timeline |
| `Action_None` | 195 | 198 | 4 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |
| `Action_None` | 212 | 213 | 2 | inferred_complete_timeline |
| `Action_None` | 215 | 218 | 4 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 204 | 94 | inferred_complete_timeline |
| `Action_None` | 207 | 299 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–276
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 216 | 106 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_None` | 231 | 234 | 4 | inferred_complete_timeline |
| `Action_None` | 237 | 243 | 7 | inferred_complete_timeline |
| `Action_None` | 252 | 253 | 2 | inferred_complete_timeline |
| `Action_None` | 255 | 261 | 7 | inferred_complete_timeline |
| `Action_None` | 267 | 276 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 203 | 93 | inferred_complete_timeline |
| `Action_None` | 207 | 224 | 18 | inferred_complete_timeline |
| `Action_None` | 229 | 299 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 189 | 79 | inferred_complete_timeline |
| `Action_None` | 191 | 201 | 11 | inferred_complete_timeline |
| `Action_None` | 207 | 214 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 214 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 218 | 108 | inferred_complete_timeline |
| `Action_None` | 238 | 243 | 6 | inferred_complete_timeline |
| `Action_None` | 245 | 248 | 4 | inferred_complete_timeline |
| `Action_None` | 251 | 269 | 19 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |
| `Action_None` | 279 | 282 | 4 | inferred_complete_timeline |
| `Action_None` | 284 | 285 | 2 | inferred_complete_timeline |
| `Action_None` | 291 | 294 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 299 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 244 | 134 | inferred_complete_timeline |
| `Action_None` | 246 | 299 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 251 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 299 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–270
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 270 | 160 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 148–257 | 77 | 6 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 153–164 | 12 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 157–298 | 106 | 7 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 158–159 | 2 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 201–222 | 12 | 4 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 201–241 | 29 | 5 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 227–264 | 37 | 2 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 232–233 | 2 | 1 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 248–260 | 8 | 2 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 248–299 | 44 | 4 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 253–299 | 36 | 3 | Undefined position; Undefined team |
| `33` | `52` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 271–274 | 4 | 1 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 272–278 | 6 | 2 | Undefined position; Undefined team |
| `36` | `55` | Position_Unknown | Team_Unknown | 272–296 | 15 | 2 | Undefined position; Undefined team |
| `37` | `57` | Position_Unknown | Team_Unknown | 285–291 | 7 | 1 | Undefined position; Undefined team |
| `38` | `67` | Position_Unknown | Team_Unknown | 296–299 | 4 | 1 | Undefined position; Undefined team |
| `39` | `68` | Position_Unknown | Team_Unknown | 297–299 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `15` (C): Annotated start 120 != Inferred start 125
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `27` (7 segments found)
- ❌ Missing segment for action `Action_Handoff` on target `6` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 93 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_Handoff' for track '6' has invalid range: start=187, end=155. Clamping end to start.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [111–124], lower_priority='Action_ZoneBlock' annotated_start=120, effective_Action_ZoneBlock_start=125.
- ⚠️ Action 'Action_None' range [111-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [116-161] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-299] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-204] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-216] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-243] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-261] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-276] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-218] for track '4' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-243] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-269] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-282] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-294] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [126-155] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-251] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-193] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-203] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-224] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-189] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-201] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-214] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-270] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-251] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-299] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-146] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-244] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-134] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-214] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-140] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [142-150] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-264] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-203] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-216] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-235] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-218] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-257] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-164] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [157-195] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [205-227] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [231-243] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [245-250] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [255-256] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [275-283] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [285-298] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-222] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-237] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-254] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-264] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-257] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-266] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-275] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-256] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-280] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-299] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-281] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-296] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-291] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '38' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.

</details>