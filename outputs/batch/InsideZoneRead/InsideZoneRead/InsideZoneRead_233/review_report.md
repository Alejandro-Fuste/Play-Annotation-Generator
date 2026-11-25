# Play-Annotation-Generator Annotation Review — InsideZoneRead_233

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_233`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 70
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | WR3 | offense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_ReadDefender` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_BlockSecondLevel` | CB5 | defense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB2 | defense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `12` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `9` | `Group` | 0 | START | 0 | 121 |
| ✅ EXACT | `Action_BallSnap` | WR3 | `12` | `11` | 122 | START | 122 | 134 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `10` | `9` | 125 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RG | `15` | `14` | 125 | START | 125 | 203 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `17` | `16` | 125 | START | 125 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 125 | START | 125 | 191 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `2` | 125 | START | 125 | 201 |
| ✅ EXACT | `Action_SnapReceive` | C | `10` | `9` | 134 | END | 122 | 134 |
| ✅ EXACT | `Action_ReadDefender` | C | `10` | `9` | 138 | START | 138 | 150 |
| ✅ EXACT | `Action_BlockSecondLevel` | CB5 | `5` | `4` | 148 | START | 148 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | C | `10` | `9` | 151 | START | 151 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB2 | `6` | `5` | 161 | START | 161 | 242 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 203 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 298 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_BallSnap` | 122 | 134 | 13 | inferred_complete_timeline |
| `Action_None` | 135 | 299 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 192 | 71 | inferred_complete_timeline |
| `Action_None` | 195 | 198 | 4 | inferred_complete_timeline |
| `Action_None` | 200 | 256 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 201 | 77 | inferred_complete_timeline |
| `Action_None` | 204 | 299 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 191 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 203 | 1 | inferred_complete_timeline |
| `Action_None` | 204 | 204 | 1 | inferred_complete_timeline |
| `Action_None` | 207 | 299 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_SnapReceive` | 122 | 134 | 13 | inferred_complete_timeline |
| `Action_None` | 135 | 137 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 138 | 150 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 151 | 151 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_None` | 161 | 299 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 203 | 79 | inferred_complete_timeline |
| `Action_None` | 204 | 287 | 84 | inferred_complete_timeline |
| `Action_None` | 289 | 299 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 203 | 79 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |
| `Action_None` | 214 | 299 | 86 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 209 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 162 | 41 | inferred_complete_timeline |
| `Action_None` | 170 | 214 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 121 | 116 | inferred_complete_timeline |
| `Action_None` | 122 | 194 | 73 | inferred_complete_timeline |
| `Action_None` | 198 | 201 | 4 | inferred_complete_timeline |
| `Action_None` | 205 | 208 | 4 | inferred_complete_timeline |
| `Action_None` | 213 | 299 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_BallCarry` | 161 | 242 | 82 | inferred_complete_timeline |
| `Action_BallCarry` | 245 | 251 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 253 | 299 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 210 | 89 | inferred_complete_timeline |
| `Action_None` | 213 | 239 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 148 | 203 | 56 | inferred_complete_timeline |
| `Action_None` | 204 | 252 | 49 | inferred_complete_timeline |
| `Action_None` | 256 | 299 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–270
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 19 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 33 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 62 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 121 | 58 | inferred_complete_timeline |
| `Action_None` | 122 | 270 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 121 | 72 | inferred_complete_timeline |
| `Action_None` | 122 | 204 | 83 | inferred_complete_timeline |
| `Action_None` | 206 | 222 | 17 | inferred_complete_timeline |
| `Action_None` | 224 | 272 | 49 | inferred_complete_timeline |
| `Action_None` | 276 | 284 | 9 | inferred_complete_timeline |
| `Action_None` | 292 | 299 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 231–299 | 69 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 242–295 | 34 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 245–271 | 27 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 251–299 | 44 | 4 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 271–284 | 14 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 279–299 | 21 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 279–294 | 13 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 281–299 | 19 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `10` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `22`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 466: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '9' has invalid range: start=125, end=121. Clamping end to start.
- ⚠️ Action 'Action_ZoneBlock' range [125-201] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-298] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-252] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [161-242] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [245-251] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-239] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-192] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-256] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' for track '9' starts at frame 151, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_Handoff' range [151-151] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-299] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-162] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-214] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-287] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-299] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-299] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-204] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-222] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-272] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-284] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-191] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 204, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [204-204] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-121] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-19] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-33] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-62] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-270] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-273] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-271] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-262] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-272] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-284] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-299] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-294] for track '28' has 2 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_233'; source metadata written as null.

</details>