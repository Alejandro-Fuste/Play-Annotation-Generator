# Play-Annotation-Generator Annotation Review — SplitZone_189

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_189`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `11` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 6 | START | 7 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 6 | START | 7 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 6 | START | 7 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 6 | START | 7 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 6 | START | 7 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 6 | START | 7 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 6 | START | 7 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 6 | START | 7 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 6 | START | 7 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 6 | START | 7 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 6 | START | 7 | 115 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `19` | `19` | 116 | START | 116 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 116 | START | 116 | 154 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `21` | `21` | 116 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LG | `3` | `3` | 116 | START | 116 | 193 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `8` | 116 | START | 116 | 193 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `21` | 118 | START | 118 | 127 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `6` | 127 | END | 118 | 127 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `6` | 135 | START | 135 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `11` | `11` | 144 | START | 144 | 179 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 193 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 7–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 117 | 111 | inferred_complete_timeline |
| `Action_SnapReceive` | 118 | 127 | 10 | inferred_complete_timeline |
| `Action_None` | 128 | 134 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 135 | 143 | 9 | inferred_complete_timeline |
| `Action_None` | 144 | 147 | 4 | inferred_complete_timeline |
| `Action_None` | 149 | 269 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 7–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 143 | 137 | inferred_complete_timeline |
| `Action_BallCarry` | 144 | 179 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 185 | 205 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 210 | 221 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 223 | 269 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 7–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 117 | 111 | inferred_complete_timeline |
| `Action_None` | 118 | 239 | 122 | inferred_complete_timeline |
| `Action_None` | 242 | 269 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 7–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 117 | 111 | inferred_complete_timeline |
| `Action_None` | 118 | 269 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 7–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 117 | 111 | inferred_complete_timeline |
| `Action_None` | 118 | 269 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 7–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 117 | 111 | inferred_complete_timeline |
| `Action_None` | 118 | 269 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 7–267
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 115 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 193 | 78 | inferred_complete_timeline |
| `Action_None` | 194 | 211 | 18 | inferred_complete_timeline |
| `Action_None` | 213 | 216 | 4 | inferred_complete_timeline |
| `Action_None` | 223 | 229 | 7 | inferred_complete_timeline |
| `Action_None` | 236 | 238 | 3 | inferred_complete_timeline |
| `Action_None` | 262 | 267 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 7–196
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 115 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 193 | 78 | inferred_complete_timeline |
| `Action_None` | 194 | 196 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 7–229
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 115 | 109 | inferred_complete_timeline |
| `Action_None` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 118 | 127 | 10 | inferred_complete_timeline |
| `Action_None` | 128 | 146 | 19 | inferred_complete_timeline |
| `Action_None` | 153 | 229 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 7–225
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 115 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 154 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 161 | 184 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 193 | 5 | inferred_complete_timeline |
| `Action_None` | 194 | 222 | 29 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 7–269
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 115 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 162 | 47 | inferred_complete_timeline |
| `Action_None` | 234 | 242 | 9 | inferred_complete_timeline |
| `Action_None` | 244 | 249 | 6 | inferred_complete_timeline |
| `Action_None` | 251 | 254 | 4 | inferred_complete_timeline |
| `Action_None` | 258 | 260 | 3 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 7–238
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 117 | 111 | inferred_complete_timeline |
| `Action_None` | 118 | 174 | 57 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 202 | 205 | 4 | inferred_complete_timeline |
| `Action_None` | 211 | 215 | 5 | inferred_complete_timeline |
| `Action_None` | 234 | 238 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 7–240
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 117 | 111 | inferred_complete_timeline |
| `Action_None` | 118 | 229 | 112 | inferred_complete_timeline |
| `Action_None` | 232 | 240 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 7–201
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 117 | 111 | inferred_complete_timeline |
| `Action_None` | 118 | 154 | 37 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 185 | 4 | inferred_complete_timeline |
| `Action_None` | 194 | 201 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 7–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 117 | 111 | inferred_complete_timeline |
| `Action_None` | 118 | 229 | 112 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_None` | 247 | 269 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 7–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 117 | 111 | inferred_complete_timeline |
| `Action_None` | 118 | 229 | 112 | inferred_complete_timeline |
| `Action_None` | 236 | 269 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 7–172
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 117 | 111 | inferred_complete_timeline |
| `Action_None` | 118 | 172 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 7–229
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 117 | 111 | inferred_complete_timeline |
| `Action_None` | 118 | 221 | 104 | inferred_complete_timeline |
| `Action_None` | 224 | 229 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 7–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 117 | 111 | inferred_complete_timeline |
| `Action_None` | 118 | 269 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 7–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 117 | 111 | inferred_complete_timeline |
| `Action_None` | 118 | 269 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 7–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 117 | 111 | inferred_complete_timeline |
| `Action_None` | 118 | 216 | 99 | inferred_complete_timeline |
| `Action_None` | 219 | 221 | 3 | inferred_complete_timeline |
| `Action_None` | 227 | 229 | 3 | inferred_complete_timeline |
| `Action_None` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 7–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 117 | 111 | inferred_complete_timeline |
| `Action_None` | 118 | 269 | 152 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 141–142 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 172–174 | 3 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 194–237 | 38 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 194–229 | 10 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 214–269 | 51 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 250–269 | 17 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `21` (C)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [118–127], lower_priority='Action_ZoneBlock' annotated_start=116, effective_Action_ZoneBlock_start=128.
- ⚠️ Action 'Action_None' range [118-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-239] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-172] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-211] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-229] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-267] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-221] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [144-179] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [185-205] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [210-221] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-154] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-201] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-229] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-229] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-240] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-174] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-216] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-229] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [116-162] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-242] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [116-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [161-184] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-222] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-229] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-229] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-229] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-260] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-269] for track '28' has 2 frames without a visible bounding box.
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

</details>