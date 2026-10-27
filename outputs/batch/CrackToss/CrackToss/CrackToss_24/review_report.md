# Play-Annotation-Generator Annotation Review — CrackToss_24

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_24`
- **Frame Range:** 0 to 358 (359 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 358
- **Player Tracks:** 44
- **Ball Tracks:** 1
- **Action Segments:** 110
- **Validation Warnings:** 130
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT1 | defense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR3 | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | offense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `6` | `5` |
| ✅ EXACT | `Action_Toss` | RB | offense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 4 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 4 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 4 | START | 5 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 4 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 4 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 4 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 4 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 4 | START | 0 | 128 |
| ✅ EXACT | `Action_BallSnap` | DT1 | `22` | `21` | 126 | START | 126 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR3 | `8` | `7` | 129 | START | 129 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | `14` | `13` | 129 | START | 129 | 161 |
| ✅ EXACT | `Action_SnapReceive` | RB | `6` | `5` | 130 | END | 126 | 130 |
| ✅ EXACT | `Action_Toss` | RB | `6` | `5` | 148 | START | 148 | 164 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `16` | `15` | 165 | START | 165 | 253 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 221 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_SnapReceive` | 126 | 130 | 5 | inferred_complete_timeline |
| `Action_None` | 131 | 147 | 17 | inferred_complete_timeline |
| `Action_Toss` | 148 | 164 | 17 | inferred_complete_timeline |
| `Action_None` | 165 | 201 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–4
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–4
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_CrackBlock` | 129 | 156 | 28 | inferred_complete_timeline |
| `Action_CrackBlock` | 160 | 221 | 62 | inferred_complete_timeline |
| `Action_None` | 222 | 223 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 5–343
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 125 | 121 | inferred_complete_timeline |
| `Action_None` | 126 | 198 | 73 | inferred_complete_timeline |
| `Action_None` | 201 | 206 | 6 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 343 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_PullBlock` | 129 | 161 | 33 | inferred_complete_timeline |
| `Action_PullBlock` | 173 | 209 | 37 | inferred_complete_timeline |
| `Action_PullBlock` | 211 | 221 | 11 | inferred_complete_timeline |
| `Action_None` | 222 | 264 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–4
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 227 | 102 | inferred_complete_timeline |
| `Action_None` | 233 | 358 | 126 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 152 | 27 | inferred_complete_timeline |
| `Action_None` | 156 | 198 | 43 | inferred_complete_timeline |
| `Action_None` | 205 | 225 | 21 | inferred_complete_timeline |
| `Action_None` | 227 | 230 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 5–235
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 125 | 121 | inferred_complete_timeline |
| `Action_None` | 126 | 232 | 107 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 5–358
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 125 | 121 | inferred_complete_timeline |
| `Action_BallSnap` | 126 | 130 | 5 | inferred_complete_timeline |
| `Action_None` | 131 | 358 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 149 | 24 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 188 | 3 | inferred_complete_timeline |
| `Action_None` | 191 | 219 | 29 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–357
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 168 | 43 | inferred_complete_timeline |
| `Action_None` | 170 | 188 | 19 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_None` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_None` | 228 | 327 | 100 | inferred_complete_timeline |
| `Action_None` | 356 | 357 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 5–358
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 125 | 121 | inferred_complete_timeline |
| `Action_None` | 126 | 154 | 29 | inferred_complete_timeline |
| `Action_None` | 158 | 358 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `defense`
- **Visible Frames:** 5–261
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 125 | 121 | inferred_complete_timeline |
| `Action_None` | 126 | 149 | 24 | inferred_complete_timeline |
| `Action_None` | 151 | 158 | 8 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 190 | 28 | inferred_complete_timeline |
| `Action_None` | 256 | 261 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 5–26
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 26 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 5–262
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 125 | 121 | inferred_complete_timeline |
| `Action_None` | 126 | 223 | 98 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_None` | 235 | 244 | 10 | inferred_complete_timeline |
| `Action_None` | 247 | 262 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 173 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–4 | 5 | 1 | Undefined position; Undefined team |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–358 | 359 | 2 | Undefined position; Undefined team |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–4 | 5 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 5–253 | 249 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 5–277 | 267 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 5–173 | 147 | 5 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 124–172 | 49 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 166–330 | 161 | 4 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 167–171 | 5 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 170–189 | 18 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 171–358 | 187 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 197–358 | 162 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 203–271 | 66 | 3 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 234–281 | 48 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 238–358 | 121 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 239–358 | 120 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 257–336 | 80 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 261–358 | 96 | 2 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 269–339 | 71 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 290–316 | 27 | 1 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 326–358 | 16 | 2 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 336–358 | 23 | 1 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 354–358 | 5 | 1 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 354–358 | 5 | 1 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 356–358 | 3 | 1 | Undefined position; Undefined team |
| `44` | `53` | Position_Unknown | Team_Unknown | 358–358 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `24` | `26` | 17 | 77 | 29 | 47.5% | 18–19, 21–22, 45–55, 60–76 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `14` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '13' (LT) duration 93 frames exceeds threshold 90 frames [start=129, end=221].
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-149] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-219] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-227] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [148-164] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-201] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [129-156] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-152] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-198] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-225] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-188] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-327] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-173] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [129-161] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [173-209] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-264] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-232] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [165-253] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-198] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-206] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-343] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-223] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-244] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-262] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-256] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-277] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-26] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-154] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-358] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-358] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-149] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-158] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-190] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-261] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-73] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-112] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-123] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-164] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-173] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-172] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-234] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-322] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-185] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-221] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-271] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-281] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-358] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-336] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-333] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-339] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-316] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-340] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
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

</details>