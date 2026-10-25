# Play-Annotation-Generator Annotation Review — BootPass_39

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_39`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_RunFlatRoute` | WR1 | offense | `7` | `7` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 67 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 62 | START | 62 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `15` | `15` | 68 | START | 77 | 78 |
| ✅ EXACT | `Action_RunBlock` | RG | `19` | `19` | 68 | START | 68 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `20` | `20` | 68 | START | 68 | 192 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `21` | `21` | 68 | START | 68 | 192 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `9` | `9` | 68 | START | 68 | 94 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 76 | END | 62 | 76 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `8` | `8` | 82 | START | 82 | 105 |
| ✅ EXACT | `Action_RunFlatRoute` | WR1 | `7` | `7` | 111 | START | 111 | 134 |
| ✅ EXACT | `Action_BootAway` | QB | `8` | `8` | 112 | START | 112 | 120 |
| ✅ EXACT | `Action_ThrowPass` | QB | `8` | `8` | 122 | START | 122 | 135 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `7` | `7` | 140 | START | 140 | 148 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_SnapReceive` | 62 | 76 | 15 | inferred_complete_timeline |
| `Action_None` | 77 | 81 | 5 | inferred_complete_timeline |
| `Action_FakeHandoff` | 82 | 105 | 24 | inferred_complete_timeline |
| `Action_None` | 106 | 111 | 6 | inferred_complete_timeline |
| `Action_BootAway` | 112 | 120 | 9 | inferred_complete_timeline |
| `Action_None` | 121 | 121 | 1 | inferred_complete_timeline |
| `Action_ThrowPass` | 122 | 135 | 14 | inferred_complete_timeline |
| `Action_None` | 136 | 269 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 100 | 39 | inferred_complete_timeline |
| `Action_None` | 102 | 177 | 76 | inferred_complete_timeline |
| `Action_None` | 191 | 215 | 25 | inferred_complete_timeline |
| `Action_None` | 220 | 238 | 19 | inferred_complete_timeline |
| `Action_None` | 245 | 251 | 7 | inferred_complete_timeline |
| `Action_None` | 253 | 258 | 6 | inferred_complete_timeline |
| `Action_None` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_None` | 265 | 269 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 111 | 134 | 24 | inferred_complete_timeline |
| `Action_None` | 135 | 139 | 5 | inferred_complete_timeline |
| `Action_SecureCatch` | 140 | 148 | 9 | inferred_complete_timeline |
| `Action_None` | 149 | 215 | 67 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 240 | 242 | 3 | inferred_complete_timeline |
| `Action_None` | 246 | 247 | 2 | inferred_complete_timeline |
| `Action_None` | 263 | 264 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 268 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 204 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 238 | 177 | inferred_complete_timeline |
| `Action_None` | 245 | 252 | 8 | inferred_complete_timeline |
| `Action_None` | 256 | 257 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 74 | 13 | inferred_complete_timeline |
| `Action_None` | 76 | 81 | 6 | inferred_complete_timeline |
| `Action_None` | 85 | 234 | 150 | inferred_complete_timeline |
| `Action_None` | 249 | 269 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_RunBlock` | 68 | 192 | 125 | inferred_complete_timeline |
| `Action_RunBlock` | 197 | 258 | 62 | inferred_complete_timeline |
| `Action_RunBlock` | 261 | 269 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_RunBlock` | 68 | 192 | 125 | inferred_complete_timeline |
| `Action_RunBlock` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 226 | 269 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_BallSnap` | 62 | 76 | 15 | inferred_complete_timeline |
| `Action_RunBlock` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 94 | 124 | 31 | inferred_complete_timeline |
| `Action_RunBlock` | 129 | 177 | 49 | inferred_complete_timeline |
| `Action_RunBlock` | 197 | 198 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 201 | 202 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_RunBlock` | 68 | 69 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_RunBlock` | 68 | 94 | 27 | inferred_complete_timeline |
| `Action_RunBlock` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 105 | 106 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 120 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 210 | 149 | inferred_complete_timeline |
| `Action_None` | 215 | 269 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 186 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 116 | 55 | inferred_complete_timeline |
| `Action_None` | 119 | 124 | 6 | inferred_complete_timeline |
| `Action_None` | 130 | 269 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 202 | 141 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |
| `Action_None` | 213 | 269 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 226 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 178 | 117 | inferred_complete_timeline |
| `Action_None` | 180 | 186 | 7 | inferred_complete_timeline |
| `Action_None` | 189 | 210 | 22 | inferred_complete_timeline |
| `Action_None` | 220 | 224 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 269 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 269 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 269 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 254 | 193 | inferred_complete_timeline |
| `Action_None` | 256 | 269 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 87–129 | 33 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 130–269 | 132 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 130–269 | 120 | 5 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 141–183 | 39 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 198–269 | 71 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 208–213 | 6 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 225–269 | 45 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 240–259 | 20 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 254–269 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `15` (6 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [62–76], lower_priority='Action_RunBlock' annotated_start=68, effective_Action_RunBlock_start=77.
- ⚠️ Action 'Action_None' range [62-204] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-238] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-252] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-269] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-100] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-177] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-215] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-238] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-251] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-258] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-210] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-269] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-178] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-186] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-215] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [68-94] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [97-98] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [105-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-226] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-254] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-186] for track '14' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [77-78] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [85-86] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [94-124] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [129-177] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [197-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [201-202] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-74] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-81] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-234] for track '16' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-202] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-124] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-269] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [68-69] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [68-192] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [197-258] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [68-192] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [201-202] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [209-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-129] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-202] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-235] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-249] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-176] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-269] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-176] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-213] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-259] for track '29' has 1 frames without a visible bounding box.
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