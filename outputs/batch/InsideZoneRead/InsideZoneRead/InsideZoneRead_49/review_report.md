# Play-Annotation-Generator Annotation Review — InsideZoneRead_49

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_49`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `25` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | SAF1 | defense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `24` | `21` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `24` | `21` |
| ❌ MISSING SEGMENT | `Action_Handoff` | Position_Unknown | Team_Unknown | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 14 | START | 14 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 14 | START | 14 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `15` | `Group` | 14 | START | 14 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 14 | START | 14 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 14 | START | 14 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 14 | START | 14 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `24` | `Group` | 14 | START | 49 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `25` | `Group` | 14 | START | 59 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 14 | START | 14 | 164 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 14 | START | 14 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | SAF1 | `21` | `20` | 121 | START | 121 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `12` | 123 | START | 123 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `16` | `15` | 123 | START | 123 | 155 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `17` | `16` | 123 | START | 123 | 226 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `24` | `21` | 123 | START | 123 | 146 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `9` | `8` | 134 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `9` | `8` | 143 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `24` | `21` | 147 | START | 147 | 161 |
| ❌ MISSING SEGMENT | `Action_Handoff` | Position_Unknown | `9` | `8` | 154 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `4` | 165 | START | 165 | 180 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 226 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `25`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 59–299
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 59 | 120 | 62 | inferred_complete_timeline |
| `Action_None` | 121 | 299 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 14–299
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 164 | 151 | inferred_complete_timeline |
| `Action_BallCarry` | 165 | 180 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 184 | 218 | 35 | inferred_complete_timeline |
| `Action_BallCarry` | 228 | 299 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 14–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 120 | 107 | inferred_complete_timeline |
| `Action_None` | 121 | 271 | 151 | inferred_complete_timeline |
| `Action_None` | 273 | 299 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 14–291
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 120 | 107 | inferred_complete_timeline |
| `Action_None` | 121 | 291 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 14–285
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 120 | 107 | inferred_complete_timeline |
| `Action_None` | 121 | 267 | 147 | inferred_complete_timeline |
| `Action_None` | 271 | 280 | 10 | inferred_complete_timeline |
| `Action_None` | 282 | 285 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 14–299
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 120 | 107 | inferred_complete_timeline |
| `Action_None` | 121 | 203 | 83 | inferred_complete_timeline |
| `Action_None` | 211 | 221 | 11 | inferred_complete_timeline |
| `Action_None` | 273 | 274 | 2 | inferred_complete_timeline |
| `Action_None` | 276 | 299 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 14–299
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 122 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 155 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 160 | 191 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 201 | 9 | inferred_complete_timeline |
| `Action_None` | 230 | 299 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `24`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 49–299
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 122 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 146 | 24 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 147 | 161 | 15 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 168 | 215 | 48 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 218 | 226 | 9 | inferred_complete_timeline |
| `Action_None` | 227 | 239 | 13 | inferred_complete_timeline |
| `Action_None` | 241 | 299 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 14–212
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 122 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 135 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 178 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 181 | 189 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 198 | 201 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 212 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 14–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 122 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 226 | 104 | inferred_complete_timeline |
| `Action_None` | 227 | 299 | 73 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 14–157
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 120 | 107 | inferred_complete_timeline |
| `Action_None` | 121 | 138 | 18 | inferred_complete_timeline |
| `Action_None` | 140 | 148 | 9 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 14–147
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 120 | 107 | inferred_complete_timeline |
| `Action_None` | 121 | 147 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 14–278
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 120 | 107 | inferred_complete_timeline |
| `Action_None` | 121 | 141 | 21 | inferred_complete_timeline |
| `Action_None` | 146 | 151 | 6 | inferred_complete_timeline |
| `Action_None` | 153 | 180 | 28 | inferred_complete_timeline |
| `Action_None` | 199 | 278 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 14–299
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 120 | 107 | inferred_complete_timeline |
| `Action_None` | 121 | 132 | 12 | inferred_complete_timeline |
| `Action_None` | 189 | 195 | 7 | inferred_complete_timeline |
| `Action_None` | 198 | 299 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 14–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 120 | 107 | inferred_complete_timeline |
| `Action_None` | 121 | 269 | 149 | inferred_complete_timeline |
| `Action_None` | 271 | 299 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 14–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 120 | 107 | inferred_complete_timeline |
| `Action_None` | 121 | 263 | 143 | inferred_complete_timeline |
| `Action_None` | 265 | 299 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 14–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 120 | 107 | inferred_complete_timeline |
| `Action_None` | 121 | 299 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 14–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 120 | 107 | inferred_complete_timeline |
| `Action_None` | 121 | 299 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 14–299
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 120 | 107 | inferred_complete_timeline |
| `Action_None` | 121 | 240 | 120 | inferred_complete_timeline |
| `Action_None` | 246 | 255 | 10 | inferred_complete_timeline |
| `Action_None` | 262 | 267 | 6 | inferred_complete_timeline |
| `Action_None` | 270 | 299 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 24–299
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 120 | 97 | inferred_complete_timeline |
| `Action_BallSnap` | 121 | 126 | 6 | inferred_complete_timeline |
| `Action_BallSnap` | 132 | 134 | 3 | inferred_complete_timeline |
| `Action_None` | 135 | 139 | 5 | inferred_complete_timeline |
| `Action_None` | 142 | 152 | 11 | inferred_complete_timeline |
| `Action_None` | 163 | 168 | 6 | inferred_complete_timeline |
| `Action_None` | 173 | 299 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 14–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 120 | 107 | inferred_complete_timeline |
| `Action_None` | 121 | 299 | 179 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 14–286 | 266 | 3 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 14–49 | 27 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 147–299 | 127 | 6 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 184–299 | 116 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 188–189 | 2 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 218–219 | 2 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 232–299 | 65 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 250–251 | 2 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 288–299 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (4 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `9` (Position_Unknown)
- ❌ Missing segment for action `Action_ReadDefender` on target `9` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `24` (3 segments found)
- ❌ Missing segment for action `Action_Handoff` on target `9` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `21`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 100: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_SnapReceive' for track '8' has invalid range: start=121, end=49. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '8' has invalid range: start=143, end=49. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '8' has invalid range: start=154, end=49. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (LT) duration 104 frames exceeds threshold 90 frames [start=123, end=226].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (RT) duration 104 frames exceeds threshold 90 frames [start=123, end=226].
- ⚠️ Action 'Action_None' range [121-271] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-291] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-271] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-286] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [165-180] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [184-218] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [228-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-267] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-280] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-285] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-38] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-263] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-138] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-148] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-135] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [141-178] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [181-189] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [198-201] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [205-206] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [210-212] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-240] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-255] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-267] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-203] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-221] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [160-191] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [193-201] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-147] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-141] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-278] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-132] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-195] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [121-126] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-139] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-168] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-50] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [147-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [168-215] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-239] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-175] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-200] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-237] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-286] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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

</details>