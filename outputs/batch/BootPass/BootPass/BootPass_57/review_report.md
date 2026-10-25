# Play-Annotation-Generator Annotation Review — BootPass_57

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_57`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_RunFlatRoute` | TE1 | offense | `19` | `19` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `17` | `17` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `25` | `23` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `12` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `19` | `Group` | 0 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 110 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 105 | START | 105 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `13` | `13` | 111 | START | 121 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `16` | `16` | 111 | START | 111 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `20` | `20` | 111 | START | 111 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `21` | `21` | 111 | START | 111 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `6` | `6` | 111 | START | 111 | 140 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 120 | END | 105 | 120 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `17` | `17` | 128 | START | 128 | 143 |
| ✅ EXACT | `Action_BootAway` | QB | `17` | `17` | 144 | START | 144 | 189 |
| ✅ EXACT | `Action_RunFlatRoute` | TE1 | `19` | `19` | 175 | START | 175 | 201 |
| ✅ EXACT | `Action_ThrowPass` | QB | `17` | `17` | 197 | START | 197 | 210 |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | `25` | `23` | 232 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_SnapReceive` | 105 | 120 | 16 | inferred_complete_timeline |
| `Action_None` | 121 | 127 | 7 | inferred_complete_timeline |
| `Action_FakeHandoff` | 128 | 143 | 16 | inferred_complete_timeline |
| `Action_BootAway` | 144 | 189 | 46 | inferred_complete_timeline |
| `Action_None` | 190 | 196 | 7 | inferred_complete_timeline |
| `Action_ThrowPass` | 197 | 210 | 14 | inferred_complete_timeline |
| `Action_None` | 211 | 359 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 201 | 97 | inferred_complete_timeline |
| `Action_None` | 203 | 354 | 152 | inferred_complete_timeline |
| `Action_None` | 358 | 359 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 354 | 250 | inferred_complete_timeline |
| `Action_None` | 357 | 359 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 293 | 189 | inferred_complete_timeline |
| `Action_None` | 302 | 306 | 5 | inferred_complete_timeline |
| `Action_None` | 313 | 359 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 175 | 201 | 27 | inferred_complete_timeline |
| `Action_None` | 202 | 359 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 129 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_RunBlock` | 111 | 140 | 30 | inferred_complete_timeline |
| `Action_RunBlock` | 144 | 195 | 52 | inferred_complete_timeline |
| `Action_RunBlock` | 198 | 359 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_RunBlock` | 111 | 177 | 67 | inferred_complete_timeline |
| `Action_RunBlock` | 180 | 192 | 13 | inferred_complete_timeline |
| `Action_RunBlock` | 195 | 310 | 116 | inferred_complete_timeline |
| `Action_RunBlock` | 312 | 359 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_BallSnap` | 105 | 120 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 121 | 133 | 13 | inferred_complete_timeline |
| `Action_RunBlock` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 139 | 141 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 180 | 193 | 14 | inferred_complete_timeline |
| `Action_RunBlock` | 204 | 359 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_RunBlock` | 111 | 138 | 28 | inferred_complete_timeline |
| `Action_RunBlock` | 140 | 354 | 215 | inferred_complete_timeline |
| `Action_RunBlock` | 356 | 359 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_RunBlock` | 111 | 157 | 47 | inferred_complete_timeline |
| `Action_RunBlock` | 159 | 348 | 190 | inferred_complete_timeline |
| `Action_RunBlock` | 351 | 359 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 359 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 319 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 174 | 70 | inferred_complete_timeline |
| `Action_None` | 191 | 359 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 148 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–355
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 199 | 95 | inferred_complete_timeline |
| `Action_None` | 201 | 355 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 341 | 237 | inferred_complete_timeline |
| `Action_None` | 346 | 359 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 232 | 128 | inferred_complete_timeline |
| `Action_None` | 235 | 239 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 359 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 359 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 283 | 179 | inferred_complete_timeline |
| `Action_None` | 291 | 359 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 359 | 255 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 136–359 | 220 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 151–153 | 3 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 180–183 | 4 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 206–207 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 206–359 | 137 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 215–242 | 28 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 249–359 | 105 | 4 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 255–257 | 3 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 261–268 | 4 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 274–275 | 2 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 292–353 | 44 | 6 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 293–295 | 3 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 302–359 | 52 | 5 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 315–337 | 11 | 4 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 348–359 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `13` (5 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `6` (3 segments found)
- ❌ Missing segment for action `Action_SecureCatch` on target `23` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [105–120], lower_priority='Action_RunBlock' annotated_start=111, effective_Action_RunBlock_start=121.
- ⚠️ Segment 'Action_SecureCatch' for track '23' has invalid range: start=232, end=153. Clamping end to start.
- ⚠️ Action 'Action_None' range [105-293] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-306] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-354] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-232] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-201] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-354] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-283] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-359] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [111-140] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [144-195] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [198-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-359] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-174] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-148] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-319] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [121-133] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [136-137] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [139-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [180-193] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [204-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-199] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-355] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-359] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [111-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [180-192] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [195-310] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-341] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [111-138] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [140-354] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [111-157] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [159-348] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-165] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-359] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-153] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-293] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-346] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-242] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-280] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-291] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-316] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-327] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-335] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-342] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-353] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-309] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-319] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-342] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-359] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-318] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-324] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-337] for track '35' has 1 frames without a visible bounding box.
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

</details>