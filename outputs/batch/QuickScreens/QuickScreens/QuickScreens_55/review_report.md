# Play-Annotation-Generator Annotation Review — QuickScreens_55

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `QuickScreens_55`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_QuickScreens`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 80
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
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_TurnToQuarterback` | WR1 | offense | `1` | `1` |
| ✅ EXACT | `Action_ScreenBlock` | WR2 | offense | `3` | `3` |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR1 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 7 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 8 | START | 8 | 17 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `4` | 19 | END | 8 | 19 |
| ✅ EXACT | `Action_TurnToQuarterback` | WR1 | `1` | `1` | 21 | START | 21 | 50 |
| ✅ EXACT | `Action_ScreenBlock` | WR2 | `3` | `3` | 27 | START | 27 | 94 |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | `4` | `4` | 39 | START | 39 | 46 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `1` | `1` | 64 | START | 64 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR1 | `1` | `1` | 76 | START | 76 | 154 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_SnapReceive` | 8 | 19 | 12 | inferred_complete_timeline |
| `Action_None` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 39 | 46 | 8 | inferred_complete_timeline |
| `Action_None` | 47 | 239 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 177 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_TurnToQuarterback` | 21 | 50 | 30 | inferred_complete_timeline |
| `Action_None` | 51 | 63 | 13 | inferred_complete_timeline |
| `Action_SecureCatch` | 64 | 72 | 9 | inferred_complete_timeline |
| `Action_None` | 73 | 75 | 3 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 76 | 154 | 79 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 156 | 171 | 16 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 178 | 186 | 9 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 188 | 190 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_ScreenBlock` | 27 | 94 | 68 | inferred_complete_timeline |
| `Action_None` | 95 | 225 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 104 | 97 | inferred_complete_timeline |
| `Action_None` | 107 | 239 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 239 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 100 | 239 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 35 | 28 | inferred_complete_timeline |
| `Action_None` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_None` | 53 | 78 | 26 | inferred_complete_timeline |
| `Action_None` | 80 | 239 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_BallSnap` | 8 | 17 | 10 | inferred_complete_timeline |
| `Action_None` | 53 | 239 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 31 | 24 | inferred_complete_timeline |
| `Action_None` | 50 | 200 | 151 | inferred_complete_timeline |
| `Action_None` | 202 | 225 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 191 | 184 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_None` | 196 | 199 | 4 | inferred_complete_timeline |
| `Action_None` | 202 | 224 | 23 | inferred_complete_timeline |
| `Action_None` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 29 | 22 | inferred_complete_timeline |
| `Action_None` | 36 | 53 | 18 | inferred_complete_timeline |
| `Action_None` | 55 | 239 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 61 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 239 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 175 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 19 | 12 | inferred_complete_timeline |
| `Action_None` | 23 | 185 | 163 | inferred_complete_timeline |
| `Action_None` | 196 | 202 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 50 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 239 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 215 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 200 | 193 | inferred_complete_timeline |
| `Action_None` | 202 | 238 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 200 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 91 | 84 | inferred_complete_timeline |
| `Action_None` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 183 | 83 | inferred_complete_timeline |
| `Action_None` | 188 | 191 | 4 | inferred_complete_timeline |
| `Action_None` | 193 | 239 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 43–75 | 15 | 6 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 66–100 | 35 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 92–239 | 145 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 95–239 | 144 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 133–134 | 2 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 140–150 | 9 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 175–198 | 13 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 239–239 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunAfterCatch` and target `1` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 60: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [8-104] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [76-154] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [156-171] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [173-175] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [178-186] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [188-190] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-225] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-239] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-177] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-215] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-191] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-199] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-224] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-98] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-50] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-175] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-183] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-239] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-200] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-238] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-31] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-200] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-225] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-61] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-29] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-53] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-19] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-185] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [8-17] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-35] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-78] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-44] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-50] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-57] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-100] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-211] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-146] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-198] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '30' has 1 frames without a visible bounding box.
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

</details>