# Play-Annotation-Generator Annotation Review — QuickScreens_101

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `QuickScreens_101`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_QuickScreens`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_TurnToQuarterback` | WR2 | offense | `3` | `3` |
| ✅ EXACT | `Action_ScreenBlock` | WR3 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR2 | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `0` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `6` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 8 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 9 | START | 9 | 23 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 23 | END | 9 | 23 |
| ✅ EXACT | `Action_TurnToQuarterback` | WR2 | `3` | `3` | 25 | START | 25 | 41 |
| ✅ EXACT | `Action_ScreenBlock` | WR3 | `1` | `1` | 26 | START | 26 | 110 |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | `12` | `12` | 34 | START | 34 | 41 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `3` | `3` | 44 | START | 44 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR2 | `3` | `3` | 75 | START | 75 | 246 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_SnapReceive` | 9 | 23 | 15 | inferred_complete_timeline |
| `Action_None` | 24 | 33 | 10 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 34 | 41 | 8 | inferred_complete_timeline |
| `Action_None` | 42 | 299 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 59 | 51 | inferred_complete_timeline |
| `Action_None` | 71 | 121 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_TurnToQuarterback` | 25 | 41 | 17 | inferred_complete_timeline |
| `Action_None` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_SecureCatch` | 44 | 58 | 15 | inferred_complete_timeline |
| `Action_None` | 59 | 74 | 16 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 75 | 246 | 172 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 248 | 249 | 2 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 252 | 264 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_ScreenBlock` | 26 | 110 | 85 | inferred_complete_timeline |
| `Action_None` | 111 | 184 | 74 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 219 | 3 | inferred_complete_timeline |
| `Action_None` | 228 | 235 | 8 | inferred_complete_timeline |
| `Action_None` | 243 | 245 | 3 | inferred_complete_timeline |
| `Action_None` | 257 | 261 | 5 | inferred_complete_timeline |
| `Action_None` | 264 | 299 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 95 | 87 | inferred_complete_timeline |
| `Action_None` | 97 | 293 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 184 | 176 | inferred_complete_timeline |
| `Action_None` | 186 | 269 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 102 | 94 | inferred_complete_timeline |
| `Action_None` | 107 | 299 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 299 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_BallSnap` | 9 | 23 | 15 | inferred_complete_timeline |
| `Action_None` | 24 | 250 | 227 | inferred_complete_timeline |
| `Action_None` | 264 | 289 | 26 | inferred_complete_timeline |
| `Action_None` | 291 | 299 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 113 | 105 | inferred_complete_timeline |
| `Action_None` | 115 | 119 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 237 | 229 | inferred_complete_timeline |
| `Action_None` | 239 | 287 | 49 | inferred_complete_timeline |
| `Action_None` | 291 | 299 | 9 | inferred_complete_timeline |

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
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 285 | 277 | inferred_complete_timeline |
| `Action_None` | 287 | 290 | 4 | inferred_complete_timeline |
| `Action_None` | 295 | 299 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–260
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 260 | 252 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 38 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 299 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 299 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 183 | 175 | inferred_complete_timeline |
| `Action_None` | 185 | 299 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 299 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 183 | 175 | inferred_complete_timeline |
| `Action_None` | 188 | 221 | 34 | inferred_complete_timeline |
| `Action_None` | 224 | 235 | 12 | inferred_complete_timeline |
| `Action_None` | 242 | 299 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 97 | 89 | inferred_complete_timeline |
| `Action_None` | 103 | 126 | 24 | inferred_complete_timeline |
| `Action_None` | 129 | 180 | 52 | inferred_complete_timeline |
| `Action_None` | 183 | 255 | 73 | inferred_complete_timeline |
| `Action_None` | 259 | 299 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 165 | 157 | inferred_complete_timeline |
| `Action_None` | 167 | 299 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 112 | 104 | inferred_complete_timeline |
| `Action_None` | 121 | 126 | 6 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 46–60 | 15 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 54–55 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 79–299 | 221 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 88–91 | 4 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 107–126 | 8 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 119–299 | 179 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 135–299 | 157 | 6 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 137–150 | 14 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 151–199 | 38 | 3 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 168–170 | 3 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 217–228 | 8 | 2 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 225–228 | 4 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 273–276 | 4 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 275–299 | 24 | 2 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 284–286 | 3 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 292–299 | 8 | 1 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 292–298 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunAfterCatch` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 70 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [9-184] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-269] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-184] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-235] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-261] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-299] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-285] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-290] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [75-246] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [248-249] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [252-264] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-102] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-299] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-183] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-95] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-293] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-38] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-97] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-126] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-180] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-255] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-237] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-287] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-59] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-121] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-165] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-299] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-260] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-183] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-235] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-112] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-126] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-250] for track '19' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-289] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-113] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-60] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-91] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-126] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-254] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-264] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-277] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-284] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-289] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-299] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-150] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-183] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-276] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-295] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-298] for track '40' has 1 frames without a visible bounding box.
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

</details>