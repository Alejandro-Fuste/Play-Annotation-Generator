# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_75

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_75`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 211
- **Validation Warnings:** 255
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 162
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_PressEdge` | Position_Unknown | Team_Unknown | `23` | `21` |
| ✅ EXACT | `Action_Handoff` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 221 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 373 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 174 |
| ❌ MISSING SEGMENT | `Action_PressEdge` | Position_Unknown | `23` | `21` | 207 | START | N/A | N/A |
| ✅ EXACT | `Action_Handoff` | C | `12` | `12` | 212 | START | 212 | 213 |
| ✅ EXACT | `Action_ZoneBlock` | C | `12` | `12` | 214 | START | 214 | 236 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `14` | `14` | 214 | START | 214 | 236 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `15` | `15` | 214 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `16` | `16` | 214 | START | N/A | N/A |

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
- **Visible Frames:** 0–353
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 353 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 221 | 222 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 293 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 330 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 334 | 341 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 347 | 357 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 366 | 375 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 378 | 387 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 390 | 391 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 398 | 400 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 404 | 405 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 407 | 419 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–392
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 236 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 240 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 248 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 255 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 266 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 271 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 306 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 360 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 362 | 369 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 371 | 373 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 380 | 382 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 391 | 392 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 373 | 374 | inferred_complete_timeline |
| `Action_PreSnap` | 376 | 380 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 384 | 407 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 418 | 419 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–373
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 113 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 120 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 213 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 214 | 236 | 23 | inferred_complete_timeline |
| `Action_None` | 237 | 362 | 126 | inferred_complete_timeline |
| `Action_None` | 366 | 373 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 124 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 133 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 166 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 211 | 43 | inferred_complete_timeline |
| `Action_Handoff` | 212 | 213 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 214 | 236 | 23 | inferred_complete_timeline |
| `Action_None` | 237 | 419 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 114 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 124 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 127 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 37 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 42 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 68 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 80 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 104 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 124 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 233 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 405 | 170 | inferred_complete_timeline |
| `Action_PreSnap` | 407 | 419 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 42 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 48 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 108 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 119 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 156 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 163 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 105 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 120 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 229 | 230 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 238 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 249 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 255 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 306 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 308 | 313 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 322 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 328 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 360 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 363 | 419 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 373 | 374 | inferred_complete_timeline |
| `Action_PreSnap` | 375 | 380 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 384 | 419 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 168 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 214 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 177 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 199 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 357 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 419 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–196 | 197 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 5–419 | 361 | 9 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 5–189 | 90 | 9 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 5–201 | 137 | 12 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 23–30 | 8 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 112–113 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 133–419 | 281 | 5 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 135–167 | 20 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 164–419 | 248 | 5 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 164–419 | 242 | 4 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 167–419 | 253 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 173–177 | 5 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 173–351 | 172 | 3 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 175–419 | 236 | 5 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 188–419 | 211 | 10 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 193–419 | 223 | 3 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 212–419 | 208 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 212–419 | 208 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 228–419 | 183 | 7 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 229–230 | 2 | 1 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 241–243 | 3 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 256–262 | 7 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 282–299 | 13 | 3 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 288–419 | 69 | 11 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 324–362 | 9 | 3 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 367–416 | 38 | 4 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 381–392 | 8 | 3 | Undefined position; Undefined team |
| `46` | `62` | Position_Unknown | Team_Unknown | 393–419 | 27 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_PressEdge` on target `23` (Position_Unknown)
- ❌ Missing segment for action `Action_ZoneBlock` on target `15` (RT)
- ❌ Missing segment for action `Action_ZoneBlock` on target `16` (RG)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 193 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '15' has invalid range: start=214, end=127. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '16' has invalid range: start=214, end=114. Clamping end to start.
- ⚠️ Segment 'Action_PressEdge' for track '21' has invalid range: start=207, end=201. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-196] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-221] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-293] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-330] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-341] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-357] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-375] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-387] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-391] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-400] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-405] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-419] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-373] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-380] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-131] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-148] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-214] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-373] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-380] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-407] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-189] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-199] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-357] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-229] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-238] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-249] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-255] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-306] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-313] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-322] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-328] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-360] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-147] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-156] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-163] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-174] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-236] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-240] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-248] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-255] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-266] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-271] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-306] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-360] for track '9' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-369] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [371-373] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-382] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-392] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-353] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-177] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-124] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-166] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-211] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-105] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-120] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-213] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-362] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-373] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-124] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-127] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-114] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-42] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-108] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-119] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-37] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-42] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-68] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-80] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-104] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-124] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-144] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-233] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-405] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-21] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-37] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-68] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-128] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-392] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-419] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-21] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-68] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-80] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-106] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-114] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-122] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-183] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-189] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-21] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-41] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-52] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-68] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-81] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-105] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-144] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-148] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-173] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-201] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-30] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-141] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-157] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-205] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-215] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-136] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-145] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-151] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-167] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-190] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-195] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-205] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-247] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-419] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-223] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-338] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-348] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-419] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-177] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-205] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-329] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-351] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-177] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-205] for track '31' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-222] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-228] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-205] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-234] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-320] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-327] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-357] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-366] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-371] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-382] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-392] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-419] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-392] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-401] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-197] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-337] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-373] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-380] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-409] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-412] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-416] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-230] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-243] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-262] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-284] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-292] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-299] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-294] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-300] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-311] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-325] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-337] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-355] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-371] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-387] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-391] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-403] for track '42' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-327] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-347] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-362] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-395] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-398] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-410] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-416] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-382] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-388] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-392] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.

</details>