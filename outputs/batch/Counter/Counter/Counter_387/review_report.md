# Play-Annotation-Generator Annotation Review — Counter_387

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_387`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `15` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 6 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 90 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 91 | START | 91 | 106 |
| ✅ EXACT | `Action_DownBlock` | RT | `12` | `11` | 94 | START | 94 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `16` | `15` | 94 | START | 107 | 124 |
| ✅ EXACT | `Action_DownBlock` | RG | `22` | `21` | 94 | START | 94 | 167 |
| ✅ EXACT | `Action_PullBlock` | LG | `21` | `20` | 94 | START | 94 | 167 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `15` | `14` | 94 | START | 94 | 167 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 106 | END | 91 | 106 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `5` | 122 | START | 122 | 157 |
| ✅ EXACT | `Action_BallCarry` | RB | `5` | `4` | 158 | START | 158 | 218 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 167 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_SnapReceive` | 91 | 106 | 16 | inferred_complete_timeline |
| `Action_None` | 107 | 121 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 122 | 157 | 36 | inferred_complete_timeline |
| `Action_None` | 158 | 273 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_BallCarry` | 158 | 218 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 243 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 197 | 107 | inferred_complete_timeline |
| `Action_None` | 200 | 210 | 11 | inferred_complete_timeline |
| `Action_None` | 212 | 217 | 6 | inferred_complete_timeline |
| `Action_None` | 220 | 299 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 265 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 94 | 167 | 74 | inferred_complete_timeline |
| `Action_None` | 168 | 299 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_PullBlock` | 94 | 167 | 74 | inferred_complete_timeline |
| `Action_None` | 168 | 291 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_BallSnap` | 91 | 106 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 107 | 124 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 127 | 167 | 41 | inferred_complete_timeline |
| `Action_None` | 168 | 187 | 20 | inferred_complete_timeline |
| `Action_None` | 195 | 299 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 6–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 8 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 93 | 84 | inferred_complete_timeline |
| `Action_DownBlock` | 94 | 167 | 74 | inferred_complete_timeline |
| `Action_None` | 168 | 299 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_DownBlock` | 94 | 162 | 69 | inferred_complete_timeline |
| `Action_None` | 178 | 299 | 122 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 142 | 52 | inferred_complete_timeline |
| `Action_None` | 145 | 168 | 24 | inferred_complete_timeline |
| `Action_None` | 170 | 172 | 3 | inferred_complete_timeline |
| `Action_None` | 176 | 179 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 178 | 88 | inferred_complete_timeline |
| `Action_None` | 186 | 188 | 3 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 202 | 4 | inferred_complete_timeline |
| `Action_None` | 204 | 266 | 63 | inferred_complete_timeline |
| `Action_None` | 269 | 271 | 3 | inferred_complete_timeline |
| `Action_None` | 274 | 277 | 4 | inferred_complete_timeline |
| `Action_None` | 281 | 283 | 3 | inferred_complete_timeline |
| `Action_None` | 285 | 299 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 122 | 32 | inferred_complete_timeline |
| `Action_None` | 124 | 201 | 78 | inferred_complete_timeline |
| `Action_None` | 205 | 209 | 5 | inferred_complete_timeline |
| `Action_None` | 212 | 217 | 6 | inferred_complete_timeline |
| `Action_None` | 219 | 236 | 18 | inferred_complete_timeline |
| `Action_None` | 238 | 248 | 11 | inferred_complete_timeline |
| `Action_None` | 252 | 299 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 176 | 86 | inferred_complete_timeline |
| `Action_None` | 187 | 192 | 6 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 213 | 10 | inferred_complete_timeline |
| `Action_None` | 215 | 216 | 2 | inferred_complete_timeline |
| `Action_None` | 220 | 299 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 31 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 90 | 48 | inferred_complete_timeline |
| `Action_None` | 91 | 150 | 60 | inferred_complete_timeline |
| `Action_None` | 154 | 190 | 37 | inferred_complete_timeline |
| `Action_None` | 193 | 198 | 6 | inferred_complete_timeline |
| `Action_None` | 210 | 299 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 191 | 101 | inferred_complete_timeline |
| `Action_None` | 193 | 196 | 4 | inferred_complete_timeline |
| `Action_None` | 199 | 203 | 5 | inferred_complete_timeline |
| `Action_None` | 210 | 214 | 5 | inferred_complete_timeline |
| `Action_None` | 216 | 299 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 247 | 157 | inferred_complete_timeline |
| `Action_None` | 254 | 291 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 257 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 203 | 113 | inferred_complete_timeline |
| `Action_None` | 209 | 214 | 6 | inferred_complete_timeline |
| `Action_None` | 218 | 299 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 201 | 111 | inferred_complete_timeline |
| `Action_None` | 206 | 236 | 31 | inferred_complete_timeline |
| `Action_None` | 238 | 291 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 210 | 120 | inferred_complete_timeline |
| `Action_None` | 212 | 299 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–66 | 62 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 8–35 | 17 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 9–288 | 259 | 4 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 123–154 | 8 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 195–299 | 95 | 5 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 239–263 | 17 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 270–271 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 776: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [91–106], lower_priority='Action_DownBlock' annotated_start=94, effective_Action_DownBlock_start=107.
- ⚠️ Action 'Action_None' range [91-197] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-217] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-257] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-203] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-243] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [158-218] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-273] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-247] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-291] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-201] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-236] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-291] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-265] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-191] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-214] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [94-162] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-176] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-213] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-299] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-31] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-90] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-190] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-198] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [107-124] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [127-167] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-187] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-90] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-178] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-266] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-277] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-142] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-168] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-60] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-66] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-122] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-201] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-217] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-236] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-248] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-291] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-8] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-11] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-31] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-35] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-90] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-218] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-270] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-154] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-224] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-263] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>