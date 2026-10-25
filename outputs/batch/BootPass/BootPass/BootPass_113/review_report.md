# Play-Annotation-Generator Annotation Review — BootPass_113

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_113`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | RG | offense | `21` | `21` |
| ❌ MISSING SEGMENT | `Action_BootAway` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunFlatRoute` | SAF1 | defense | `5` | `5` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SecureCatch` | SAF1 | defense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE4 | `11` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `14` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `9` | `Group` | 0 | START | 0 | 41 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 42 | START | 42 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `10` | `10` | 43 | START | 44 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `17` | `17` | 43 | START | 43 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `18` | `18` | 43 | START | 43 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `19` | `19` | 43 | START | 43 | 54 |
| ❌ MISSING SEGMENT | `Action_RunBlock` | RG | `21` | `21` | 43 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | RG | `21` | `21` | 43 | END | 42 | 43 |
| ❌ MISSING SEGMENT | `Action_BootAway` | RG | `21` | `21` | 69 | START | N/A | N/A |
| ✅ EXACT | `Action_RunFlatRoute` | SAF1 | `5` | `5` | 89 | START | 89 | 101 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | RG | `21` | `21` | 89 | START | N/A | N/A |
| ✅ EXACT | `Action_SecureCatch` | SAF1 | `5` | `5` | 103 | START | 103 | 116 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 154 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 260 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 299 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 77 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 202 | 161 | inferred_complete_timeline |
| `Action_None` | 204 | 269 | 66 | inferred_complete_timeline |
| `Action_None` | 271 | 298 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>TE4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 67 | 26 | inferred_complete_timeline |
| `Action_None` | 69 | 201 | 133 | inferred_complete_timeline |
| `Action_None` | 204 | 269 | 66 | inferred_complete_timeline |
| `Action_None` | 279 | 299 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_RunBlock` | 43 | 75 | 33 | inferred_complete_timeline |
| `Action_RunBlock` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 87 | 276 | 190 | inferred_complete_timeline |
| `Action_RunBlock` | 278 | 299 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 41 | 14 | inferred_complete_timeline |
| `Action_RunBlock` | 43 | 54 | 12 | inferred_complete_timeline |
| `Action_RunBlock` | 56 | 62 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 72 | 76 | 5 | inferred_complete_timeline |
| `Action_RunBlock` | 82 | 85 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 88 | 299 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_BallSnap` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 44 | 80 | 37 | inferred_complete_timeline |
| `Action_RunBlock` | 83 | 299 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_SnapReceive` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_None` | 44 | 58 | 15 | inferred_complete_timeline |
| `Action_None` | 61 | 62 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_RunBlock` | 43 | 67 | 25 | inferred_complete_timeline |
| `Action_RunBlock` | 77 | 95 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 257 | 216 | inferred_complete_timeline |
| `Action_None` | 262 | 267 | 6 | inferred_complete_timeline |
| `Action_None` | 278 | 299 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 299 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 87 | 46 | inferred_complete_timeline |
| `Action_None` | 93 | 259 | 167 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |
| `Action_None` | 278 | 299 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 108 | 67 | inferred_complete_timeline |
| `Action_None` | 110 | 242 | 133 | inferred_complete_timeline |
| `Action_None` | 248 | 269 | 22 | inferred_complete_timeline |
| `Action_None` | 286 | 299 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 116 | 75 | inferred_complete_timeline |
| `Action_None` | 119 | 124 | 6 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 138 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 221 | 180 | inferred_complete_timeline |
| `Action_None` | 226 | 228 | 3 | inferred_complete_timeline |
| `Action_None` | 230 | 232 | 3 | inferred_complete_timeline |
| `Action_None` | 234 | 236 | 3 | inferred_complete_timeline |
| `Action_None` | 240 | 241 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 299 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 257 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 91 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 89 | 101 | 13 | inferred_complete_timeline |
| `Action_None` | 102 | 102 | 1 | inferred_complete_timeline |
| `Action_SecureCatch` | 103 | 116 | 14 | inferred_complete_timeline |
| `Action_None` | 117 | 189 | 73 | inferred_complete_timeline |
| `Action_None` | 192 | 219 | 28 | inferred_complete_timeline |
| `Action_None` | 221 | 258 | 38 | inferred_complete_timeline |
| `Action_None` | 267 | 268 | 2 | inferred_complete_timeline |
| `Action_None` | 276 | 299 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 186 | 145 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 66–299 | 189 | 5 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 89–172 | 84 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 99–299 | 201 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 111–299 | 189 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 131–182 | 50 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 133–142 | 8 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 137–299 | 163 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 137–140 | 4 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 149–150 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 155–156 | 2 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 189–192 | 4 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 189–299 | 111 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 194–299 | 106 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 280–296 | 17 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 290–296 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `19` (5 segments found)
- ❌ Missing segment for action `Action_RunBlock` on target `21` (RG)
- ❌ Missing segment for action `Action_BootAway` on target `21` (RG)
- ❌ Missing segment for action `Action_ThrowPass` on target `21` (RG)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 72 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [42–43], lower_priority='Action_RunBlock' annotated_start=43, effective_Action_RunBlock_start=44.
- ⚠️ Overlapping action conflict at frame 43 for track '21': 'Action_RunBlock' vs 'Action_SnapReceive'. Overriding with 'Action_SnapReceive'.
- ⚠️ Segment 'Action_BootAway' for track '21' has invalid range: start=69, end=62. Clamping end to start.
- ⚠️ Segment 'Action_ThrowPass' for track '21' has invalid range: start=89, end=62. Clamping end to start.
- ⚠️ Action 'Action_None' range [42-260] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-91] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-87] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-259] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-257] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-267] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-189] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-219] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-258] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-299] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-221] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-116] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-138] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-202] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-269] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-298] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [44-80] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-67] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-201] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-269] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-257] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-108] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-242] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-269] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-77] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-299] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [43-75] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [77-80] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [87-276] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [43-67] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [77-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-41] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [43-54] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [56-62] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [72-76] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [82-85] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-58] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-74] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-172] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-299] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-177] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-299] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-296] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-296] for track '37' has 1 frames without a visible bounding box.
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

</details>