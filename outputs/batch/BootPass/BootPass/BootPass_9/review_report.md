# Play-Annotation-Generator Annotation Review — BootPass_9

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_9`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ START CHANGED | `Action_RunBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_SecureCatch` | TE1 | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `5` | `Group` | 0 | START | 0 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 0 | START | 0 | 26 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 27 | START | 27 | 43 |
| ⚠️ START CHANGED | `Action_RunBlock` | C | `15` | `15` | 37 | START | 44 | 299 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `17` | `17` | 37 | START | 37 | 206 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `19` | `19` | 37 | START | 37 | 142 |
| ✅ EXACT | `Action_RunBlock` | LG | `20` | `20` | 37 | START | 37 | 44 |
| ✅ EXACT | `Action_RunBlock` | LT | `21` | `21` | 37 | START | 37 | 226 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 43 | END | 27 | 43 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `18` | `18` | 47 | START | 47 | 65 |
| ✅ EXACT | `Action_BootAway` | QB | `18` | `18` | 66 | START | 66 | 99 |
| ✅ EXACT | `Action_ThrowPass` | QB | `18` | `18` | 121 | START | 121 | 133 |
| ✅ EXACT | `Action_SecureCatch` | TE1 | `5` | `5` | 176 | START | 176 | 182 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 43 | 17 | inferred_complete_timeline |
| `Action_None` | 44 | 46 | 3 | inferred_complete_timeline |
| `Action_FakeHandoff` | 47 | 65 | 19 | inferred_complete_timeline |
| `Action_BootAway` | 66 | 99 | 34 | inferred_complete_timeline |
| `Action_None` | 100 | 120 | 21 | inferred_complete_timeline |
| `Action_ThrowPass` | 121 | 133 | 13 | inferred_complete_timeline |
| `Action_None` | 134 | 205 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–283
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 97 | 71 | inferred_complete_timeline |
| `Action_None` | 110 | 133 | 24 | inferred_complete_timeline |
| `Action_None` | 138 | 241 | 104 | inferred_complete_timeline |
| `Action_None` | 279 | 280 | 2 | inferred_complete_timeline |
| `Action_None` | 282 | 283 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 299 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 299 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_SecureCatch` | 176 | 182 | 7 | inferred_complete_timeline |
| `Action_None` | 183 | 299 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 144 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_RunBlock` | 37 | 226 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–44
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_RunBlock` | 37 | 44 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_BallSnap` | 27 | 43 | 17 | inferred_complete_timeline |
| `Action_RunBlock` | 44 | 299 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_RunBlock` | 37 | 142 | 106 | inferred_complete_timeline |
| `Action_RunBlock` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 153 | 187 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_RunBlock` | 37 | 206 | 170 | inferred_complete_timeline |
| `Action_RunBlock` | 210 | 216 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 218 | 221 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 223 | 226 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 228 | 257 | 30 | inferred_complete_timeline |
| `Action_RunBlock` | 263 | 287 | 25 | inferred_complete_timeline |
| `Action_RunBlock` | 290 | 299 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 221 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 299 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 299 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 169 | 143 | inferred_complete_timeline |
| `Action_None` | 172 | 299 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 178 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 154 | 128 | inferred_complete_timeline |
| `Action_None` | 165 | 299 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 299 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 200 | 174 | inferred_complete_timeline |
| `Action_None` | 202 | 204 | 3 | inferred_complete_timeline |
| `Action_None` | 207 | 212 | 6 | inferred_complete_timeline |
| `Action_None` | 215 | 299 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 117 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 160 | 134 | inferred_complete_timeline |
| `Action_None` | 162 | 168 | 7 | inferred_complete_timeline |
| `Action_None` | 170 | 299 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 285 | 259 | inferred_complete_timeline |
| `Action_None` | 291 | 292 | 2 | inferred_complete_timeline |
| `Action_None` | 296 | 299 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 59–62 | 4 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 112–299 | 185 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 129–157 | 29 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 167–172 | 4 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 169–282 | 50 | 9 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 170–299 | 130 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 177–193 | 17 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 248–288 | 12 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 284–286 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_RunBlock` for actor_track_id `15` (C): Annotated start 37 != Inferred start 44
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `17` (7 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `19` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [27–43], lower_priority='Action_RunBlock' annotated_start=37, effective_Action_RunBlock_start=44.
- ⚠️ Action 'Action_None' range [27-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-299] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-175] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-178] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-144] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-117] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-221] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-200] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-212] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-169] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-285] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-97] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-241] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-160] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-168] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [37-206] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [210-216] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [218-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [223-226] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [228-257] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [263-287] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [290-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-205] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [37-142] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [145-146] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [149-151] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [153-187] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [37-44] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [37-226] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-62] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-123] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-134] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-157] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-189] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-211] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-221] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-193] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-254] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '30' has 1 frames without a visible bounding box.
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

</details>